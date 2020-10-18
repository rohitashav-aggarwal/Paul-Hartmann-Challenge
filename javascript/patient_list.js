let list = document.getElementById("displayListPatients");

let url = "http://localhost:5000/getAllPatients";
let table, row, cell;

function getList() {
    fetch(url,{
            method: 'GET',
            headers: {
                "accept": "application/json"
            }
        })
        .then(response => response.json())
        .then((data) => {
            table = document.getElementById("patient_list");
            for(let i = 0; i < data.result.length; i++){
                console.log(data.result[i].care_level);
                row = table.insertRow();
                cell = row.insertCell();
                cell.textContent = data.result[i].name;
                cell = row.insertCell();
                cell.textContent = data.result[i].address;
                cell = row.insertCell();
                cell.textContent = data.result[i].phone;
                cell = row.insertCell();
                cell.textContent = data.result[i].care_level;
                cell = row.insertCell();
                let btn = document.createElement('input');
                btn.type = "button";
                btn.value = "Details";
                btn.id = "button" + i;
                btn.class="btn btn-primary";
                btn.setAttribute("data-toggle", "modal");
                btn.setAttribute("data-target", "#exampleModal2");
                // type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal"
                btn.onclick = (function() {
                    let x = document.getElementById("exampleModal2");
                    if(x.style.display === "none"){
                        x.style.display = "block";
                    }else{
                        x.style.display = "none";
                    }
                });
                cell.appendChild(btn);
            }
        });
}

function addPatient(){
    const patientName = document.getElementById("patientName").value;
    const patientAddress = document.getElementById("patientaddress").value;
    const patientPhone = document.getElementById("patientPhone").value;
    const patientCare_level = document.getElementById("patientcare_level").value;
    const patientCaretaker = document.getElementById("careTaker").value;
    const patient_vitals = document.getElementById("vitals").value;
    const patientMeds = document.getElementById("medication").value;
    const data = {
        name: patientName,
        address: patientAddress,
        phone: patientPhone,
        care_level: patientCare_level,
        caretaker: patientCaretaker,
        patient_vitals: patient_vitals,
        meds: patientMeds
    };

    fetch('http://localhost:5000/Patients', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success');
            location.reload();
    })
        .catch((error) => {
            console.error('Error:', error);
    });
}

function updatePatient(){
    alert("Saved");
}