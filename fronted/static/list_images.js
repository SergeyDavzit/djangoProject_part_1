const app = Vue.createApp(
    {
        el: '#list_images',
        data() { return {
            images: []
            }
        },
        created: function () {
            const vm = this;
            axios.get('/api/image/')
                .then(function (response) {
                    vm.images = response.data;
                    for (let i = 0; i < vm.images.length; i++) {
                        vm.images[i].img = vm.images[i].image_data;
                    }
                })
        },
        methods: {
            deleteImage: function (id) {
                axios.defaults.xsrfCookieName = 'csrftoken';
                axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
                const vm = this;
                console.log(id);
                axios.delete('/api/image/', {data: {image_id: id}})
                    .then(function (response) {
                        vm.images = vm.images.filter(image => image.image_id !== id);
                    })
            }
        }

    }
);
app.mount('#list_images');