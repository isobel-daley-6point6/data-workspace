import AWS from "aws-sdk";

export class S3Proxy {
  constructor(config, s3) {
    this.config = config;
    this.s3 = s3;
  }

  async listObjects(params) {
    const response = await this.s3.listObjectsV2(params).promise();
    const files = response.Contents
      .filter((file) => (file.Key !== params.Prefix))
      .map((file) => ({
        ...file,
        formattedDate: new Date(file.LastModified),
        isSelected: false,
      }));

    const bigDataFolder = (params.Prefix === this.config.initialPrefix) ? [{
        Prefix: this.config.initialPrefix + this.config.bigdataPrefix,
        isBigData: true,
        isSelected: false,
      }] : [];
    const foldersWithoutBigData = response.CommonPrefixes.filter((folder) => {
      return folder.Prefix !== `${this.config.initialPrefix}${this.config.bigdataPrefix}`;
    }).map((folder) => ({
      ...folder,
      isBigData: false,
      isSelected: false,
    }))
    const folders = bigDataFolder.concat(foldersWithoutBigData);

    return {
      files,
      folders,
    };
  }

  getSignedUrl(params) {
    return this.s3.getSignedUrlPromise("getObject", params);
  }

  removeSlashes(text) {
    return text.replace(/^\/+/g, "").replace(/\/+$/g, "");
  }

  async createFolder(prefix, folderName) {
    console.log("createFolder", prefix, folderName);
    const folder = prefix + this.removeSlashes(folderName) + "/";
    console.log(folder);
    const params = { Bucket: this.config.bucketName, Key: folder };
    let canCreate = false;

    // Slightly awkward since a 404 is converted to an exception
    try {
      await this.s3.headObject(params).promise();
    } catch (err) {
      canCreate = err.code === "NotFound";
      if (!canCreate) {
        throw err;
      }
    }
    if (!canCreate) {
      alert("Error: folder or object already exists at " + params.Key);
      return;
    }

    await this.s3.putObject(params).promise();
  }

  async deleteObjects(bucket, keys) {
    return this.s3
      .deleteObjects({
        Bucket: bucket,
        Delete: { Objects: keys.map((key) => ({ Key: key })) },
      })
      .promise();
  }
}
