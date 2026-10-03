"""Short-lived access to a private S3-compatible source-asset bucket."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class PrivateAssetSigner:
    client: object
    bucket: str
    ttl_seconds: int = 300

    @classmethod
    def from_environment(cls) -> "PrivateAssetSigner | None":
        endpoint = os.getenv("S3_ENDPOINT_URL")
        bucket = os.getenv("S3_BUCKET")
        access_key = os.getenv("S3_ACCESS_KEY_ID")
        secret_key = os.getenv("S3_SECRET_ACCESS_KEY")
        if not all((endpoint, bucket, access_key, secret_key)):
            return None
        import boto3

        client = boto3.client(
            "s3",
            endpoint_url=endpoint,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        ttl = min(900, max(30, int(os.getenv("S3_SIGNED_URL_TTL_SECONDS", "300"))))
        return cls(client=client, bucket=bucket, ttl_seconds=ttl)

    def signed_get_url(self, key: str) -> str:
        if not key or key.startswith(("/", "\\")) or ".." in key.replace("\\", "/").split("/"):
            raise ValueError("invalid private asset key")
        return self.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": self.bucket, "Key": key.replace("\\", "/")},
            ExpiresIn=self.ttl_seconds,
        )
