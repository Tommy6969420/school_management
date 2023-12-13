$(document).ready(function() {
    $('#id_student').select2();
}); 
$(document).ready(function() {
    $('#id_transportation').select2();
}); 

const id_student=document.getElementById("id_student");
const id_input=document.getElementById("inp_get");
const tbl_class = document.getElementById("tbl_class");
const tbl_admission = document.getElementById("tbl_admission");
const tbl_monthly = document.getElementById("tbl_montly");
const previous_due= document.getElementById("id_previous_due");
const previous_recipt=document.getElementById("previous_recipt");
const previous_due_inf=document.getElementById("previous_due");
const previous_billing_date=document.getElementById("previous_billing_date");
var data_payload;
id_student.onchange=function () {
    id_input.value=parseInt(this.value);
const url=`std_search/?student_id=${id_input.value}`;
fetch(url)
.then(response => {
    if (!response.ok){
        throw new Error("Not Ok")
    }return response.json();
}).then(data =>{
    data_payload=data.payload;
    tbl_class.innerText=data_payload.class;
    tbl_admission.innerText=data_payload.admission_fee;
    tbl_monthly.innerText= data_payload.monthly_fee;
    previous_due.value=data_payload.due_amount;
    previous_recipt.innerText=data_payload.recipt_no;
    previous_due_inf.innerText=data_payload.due_amount;
    previous_billing_date.innerText=data_payload.billing_date;
    document.getElementById("id_monthly").value=data_payload.monthly_fee;
}
).catch(error => {
console.error('There was a problem with the fetch operation:', error);
});}

// API WORK FINISHED

// IMPLEMENTING TRANSPORTATION AS INT
var id_transp=document.getElementById("id_transportation")
var transp,transp_id_val,transportation_fee
id_transp.onchange=function () {
transp_id_val = parseInt(this.value)
transp=id_transp.innerText;
arr_transp=transp.split("\n");
transportation_fee=parseInt(arr_transp.slice(transp_id_val-1,transp_id_val))
console.log(transportation_fee);
}

// IMPLEMENTING GET TOTAL AND DUES
let id_total=document.getElementById("id_total")
let id_paid=document.getElementById("id_paid")
let id_due=document.getElementById("id_due")

id_total.addEventListener("click",()=>{
    let admission_fee=parseFloat(document.getElementById("id_admission").value);
    let monthly_fee=parseFloat(document.getElementById("id_monthly").value);
    let tc_certificate_fee=parseFloat(document.getElementById("id_T_C_certificate_fee").value);
    let others=parseFloat(document.getElementById("id_others").value);
    let prev_due=parseFloat(previous_due.value);
    let sum=admission_fee+monthly_fee+tc_certificate_fee+others+prev_due+transportation_fee;
    document.getElementById("id_total").value=sum;
})
id_total.addEventListener("select",sum_total_select())
id_total.addEventListener("mouseover",sum_total_select())
function sum_total_select(){
document.getElementById("id_total").onselect= function (){
    let admission_fee=parseFloat(document.getElementById("id_admission").value)
    let monthly_fee=parseFloat(document.getElementById("id_monthly").value)
    let tc_certificate_fee=parseFloat(document.getElementById("id_T_C_certificate_fee").value)
    let others=parseFloat(document.getElementById("id_others").value)
    let prev_due=parseFloat(previous_due.value)
    let sum=admission_fee+monthly_fee+tc_certificate_fee+others+prev_due+transportation_fee
    id_total.value=sum
}}

id_paid.addEventListener("input",()=>{
    id_due.value=parseInt(id_total.value)-parseInt(id_paid.value)

})