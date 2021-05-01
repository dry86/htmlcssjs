<template>
<el-form>
<el-form-item>
<el-upload

  action="https://jsonplaceholder.typicode.com/posts/"
  accept=".txt,application/msword,.docx"
  :http-request="upload"
  :on-change="onUploadChange"
  :on-preview="handlePreview"
  :on-remove="handleRemove"

  multiple
  :limit="5"
  :on-exceed="handleExceed"
  :file-list="fileList">
  <el-button  type="primary">选取</el-button>

  <div slot="tip" class="el-upload__tip">只能上传txt/doc/docx文件，且不超过1MB</div>
</el-upload>
</el-form-item>


  <el-form-item>
    <el-button type="primary" @click="onSubmit">提交</el-button>

  </el-form-item>
</el-form>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        fileList: [ ],
        files:{ }
      };
    },
    methods: {
      upload(item)
      {
        console.log(item.file);
        this.files = item.file;
      },
      onSubmit()
      {
        let fd = new FormData()
        fd.append('File', this.files)
        console.log(this.files);
        axios.post('http://127.0.0.1:5000/upload', fd, {
           headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          console.log(response.data);
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      onUploadChange(file)
      {
        const isfile = (file.raw.type === 'text/plain' || file.raw.type === 'application/msword');
        const isLt1M = file.size / 1024 / 1024 < 1;

        if (!isfile) {
          this.$message.error('只能上传txt/doc!');
          return false;
        }
        if (!isLt1M) {
          this.$message.error('上传文件大小不能超过 1MB!');
          return false;
        }
       },
       handleRemove(file, fileList) {
         console.log(file, fileList);
       },
       handlePreview(file) {
         console.log(file);
       },
       handleExceed(files, fileList) {
         this.$message.warning(`当前限制选择 5 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
       },
    },
    
    mounted(){

    }
    
  }
</script>

<style>

</style>
