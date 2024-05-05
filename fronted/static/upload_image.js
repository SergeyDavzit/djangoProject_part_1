const app = Vue.createApp(
    {
        el: '#upload_image',
        methods: {
            onFileChanged(event) {this.selectedFile = event.target.files[0];},
            onUpload(description) {
                const reader = new FileReader();
                reader.readAsDataURL(this.selectedFile);
                reader.onload = function () {
                    axios.defaults.xsrfCookieName = 'csrftoken';
                    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
                    axios.post('/api/image/', {'image_data': reader.result, 'description': description})
                };
                reader.onerror = function (error) {};
            }
        },
        data() {
            return {
                selectedFile: null
            };
   }
    }

).mount('#upload_image');