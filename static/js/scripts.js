$(document).ready(function() {
    $('#id_student').select2();
}); 
$(document).ready(function() {
    $('#id_transportation').select2();
}); 
const id_student=document.getElementById("id_student");
var id_input=document.getElementById("inp_get");
var std;
id_student.onchange=function () {
    id_input.value=parseInt(this.value);
const url=`std_search/?student_id=${id_input.value}`;
fetch(url)
.then(response => {
    if (!response.ok){
        throw new Error("Not Ok")
    }return response.json();
}).then(data => 
console.log(data.obj)
).catch(error => {
console.error('There was a problem with the fetch operation:', error);
});}