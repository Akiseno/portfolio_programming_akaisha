let counter=0
function addTask(){
    counter++
    let input=document.getElementById("taskInput")
    let taskText=input.value
    if (taskText.trim()===""){
        alert("please type a task first")
        return
    }
    let newItem=document.createElement("li");
    newItem.innerHTML=taskText
    let list=document.getElementById("tasklist");
    list.appendChild(newItem)
    let counterText=document.getElementById("counter")
    counterText.innerHTML=counter

    input.value=""
}
document.getElementById("taskInput").addEventListener("keypress",function(event){
    if (event.key==="Enter"){
        addTask()
    }
})