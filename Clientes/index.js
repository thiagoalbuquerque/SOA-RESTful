Vue.prototype.$http = axios;
Vue.use(Vuetable);

var app = new Vue({
    el: '#app',
    data: {
        fields: ['cpf', 'nome', '__slot:actions'],
        cpf: "",
        nome: "",
        qualis: "",
        revista: ""
    },
    methods: {
        getAutores(){
            this.$http.get("http://127.0.0.1:555/autor").then((response) => {
                console.log(response.data)
            });
        },
        addAutor(){
            console.log("cpf: " + this.cpf);
            console.log("nome: " + this.nome);
            this.$http.post("http://127.0.0.1:555/autor", {
                cpf : this.cpf,
                nome : this.nome
            }).then((response) => {
                alert("Refresh the page to see inserted data")
            });
        },
        updateAutor(rowData){
            alert("You clicked edit on"+ JSON.stringify(rowData))
            this.$http.put("http://127.0.0.1:555/autor", {
                cpf : rowData.cpf,
                nome : this.nome
            }).then((response) => {
                alert("Refresh the page to see updated data")
            });
        },
        deleteRow(rowData){
            alert("You clicked delete on"+ JSON.stringify(rowData))
        }

    }
});

