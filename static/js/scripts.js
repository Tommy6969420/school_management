$(document).ready(function() {
    $('#id_student').select2();
}); 
$(document).ready(function() {
    $('#id_transportation').select2();
}); 

const id_student=document.getElementById("id_student");
var id_input=document.getElementById("inp_get");
const tbl_class = document.getElementById("tbl_class");
const tbl_admission = document.getElementById("tbl_admission");
const tbl_monthly = document.getElementById("tbl_montly");
id_student.onchange=function () {
    id_input.value=parseInt(this.value);
const url=`std_search/?student_id=${id_input.value}`;
fetch(url)
.then(response => {
    if (!response.ok){
        throw new Error("Not Ok")
    }return response.json();
}).then(data =>{

    tbl_class.innerText=data.payload.class;
    tbl_admission.innerText=data.payload.admission_fee;
    tbl_monthly.innerText=data.payload.monthly_fee;

}
).catch(error => {
console.error('There was a problem with the fetch operation:', error);
});}
