# Official Ballerina {{VERSION_PLACEHOLDER}} Release Artifacts


## Linux

- **[ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.deb](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{VERSION_PLACEHOLDER}}/ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.deb)**
- **[ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.rpm](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{VERSION_PLACEHOLDER}}/ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.rpm)**


## MacOS

- **[ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-macos-x64.pkg](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{VERSION_PLACEHOLDER}}/ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-macos-x64.pkg)**

## MacOS-ARM

- **[ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-macos-arm-x64.pkg](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{VERSION_PLACEHOLDER}}/ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-macos-arm-x64.pkg)**

## Windows

- **[ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-windows-x64.msi](https://github.com/Miranlfk/ballerina-distribution/releases/download/v{{VERSION_PLACEHOLDER}}/ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-windows-x64.msi)**


For more builds across platforms and architectures see the `Assets` section below.


## Signatures and Verification

`Ballerina` uses [sigstore/cosign](https://github.com/sigstore/cosign) for signing and verifying the release artifacts.


Below is an example of using `cosign` to verify the release artifact:

```
cosign verify-blob ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.deb  --certificate ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.deb.pem --signature ballerina-{{VERSION_PLACEHOLDER}}-swan-lake-linux-x64.deb.sig --certificate-identity=https://github.com/Miranlfk/ballerina-distribution/.github/workflows/publish-release.yml@refs/heads/master --certificate-oidc-issuer=https://token.actions.githubusercontent.com
```

The following signatures done to the `Ballerina` release artifacts are recorded in [Rekor](https://github.com/sigstore/rekor) which is a `Sigstore Transparency Log`. API calls can be made to the `Rekor` API and details of the `signature`, `certifcate chain` can be retrieved and verified. Follow the below example:





