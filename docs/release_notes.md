# Official Ballerina {{Version}} Release Artifacts


## Linux

- **[ballerina-{{Version}}-swan-lake-linux-x64.deb](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{Version}}/ballerina-{{Version}}-swan-lake-linux-x64.deb)**
- **[ballerina-{{Version}}-swan-lake-linux-x64.rpm](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{Version}}/ballerina-{{Version}}-swan-lake-linux-x64.rpm)**


## MacOS

- **[ballerina-{{Version}}-swan-lake-macos-x64.pkg](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{Version}}/ballerina-{{Version}}-swan-lake-macos-x64.pkg)**

## MacOS-ARM

- **[ballerina-{{Version}}-swan-lake-macos-arm-x64.pkg](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{Version}}/ballerina-{{Version}}-swan-lake-macos-arm-x64.pkg)**

## Windows

- **[ballerina-{{Version}}-swan-lake-windows-x64.msi](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{Version}}/ballerina-{{Version}}-swan-lake-windows-x64.msi)**


For more builds across platforms and architectures see the `Assets` section below.


## Signatures and Verification

`Ballerina` uses [sigstore/cosign](https://github.com/sigstore/cosign) for signing and verifying the release artifacts.


Below is an example of using `cosign` to verify the release artifact:

```
cosign verify-blob ballerina-{{Version}}-swan-lake-linux-x64.deb  --certificate ballerina-{{Version}}-swan-lake-linux-x64.deb.pem --signature ballerina-{{Version}}-swan-lake-linux-x64.deb.sig --certificate-identity=https://github.com/Miranlfk/ballerina-distribution/.github/workflows/publish-release.yml@refs/heads/master --certificate-oidc-issuer=https://token.actions.githubusercontent.com
```

The following signatures done to the `Ballerina` release artifacts are recorded in [Rekor](https://github.com/sigstore/rekor) which is a `Sigstore Transparency Log`. API calls can be made to the `Rekor` API and details of the `signature`, `certifcate chain` can be retrieved and verified. Follow the below example:

1. Download the desired artifact.
2. Generate a sha256 Hash for the artifact and store it in a variable
>  `SHASUM=$(shasum -a 256 ballerina-{{Version}}-swan-lake-linux-x64.deb |awk '{print $1}')` 
3. Make a call to the `rekor` api to retrieve the entry of the signature and store it as the UUID value.
> `curl -X POST -H "Content-type: application/json" 'https://rekor.sigstore.dev/api/v1/index/retrieve' --data-raw "{\"hash\":\"sha256:$SHASUM\"} `



