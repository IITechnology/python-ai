// ======================================================
// SCHOOL PORTAL
// signup.js
// ======================================================

const API_URL = "http://127.0.0.1:8000";


// ======================================================
// ELEMENTS
// ======================================================

const signupForm = document.getElementById("signupForm");

const loader = document.getElementById("loader");

const toast = document.getElementById("toast");


// ======================================================
// TOAST
// ======================================================

function showToast(message, success = true){

    toast.textContent = message;

    toast.style.display = "block";

    toast.style.background = success
        ? "#16a34a"
        : "#dc2626";

    setTimeout(() => {

        toast.style.display = "none";

    },3000);

}


// ======================================================
// LOADER
// ======================================================

function showLoader(){

    loader.classList.remove("hidden");

}

function hideLoader(){

    loader.classList.add("hidden");

}


// ======================================================
// CHECK LOGIN
// ======================================================

const loggedUser = localStorage.getItem("student");

if(loggedUser){

    window.location.href = "index.html";

}


// ======================================================
// SIGNUP
// ======================================================

signupForm.addEventListener("submit", async(e)=>{

    e.preventDefault();

    const name=document.getElementById("name").value.trim();

    const roll=Number(document.getElementById("roll").value);

    const email=document.getElementById("email").value.trim();

    const branch=document.getElementById("branch").value;

    const semester=Number(document.getElementById("semester").value);

    const password=document.getElementById("password").value;

    const confirmPassword=document.getElementById("confirmPassword").value;


    // ==========================================
    // VALIDATION
    // ==========================================

    if(
        !name ||
        !roll ||
        !email ||
        !branch ||
        !semester ||
        !password ||
        !confirmPassword
    ){

        showToast("Please fill all fields.",false);

        return;

    }


    if(password!==confirmPassword){

        showToast("Passwords do not match.",false);

        return;

    }


    if(password.length<6){

        showToast("Password must contain at least 6 characters.",false);

        return;

    }


    showLoader();


    try{

        const response=await fetch(`${API_URL}/signup`,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                roll,

                name,

                email,

                branch,

                semester,

                password

            })

        });


        const data=await response.json();

        hideLoader();


        if(!response.ok){

            showToast(data.detail || "Registration failed.",false);

            return;

        }


        // ======================================
        // AUTO LOGIN
        // ======================================

        localStorage.setItem(

            "student",

            JSON.stringify(data.student)

        );


        showToast("Account Created Successfully!");



        setTimeout(()=>{

            window.location.href="index.html";

        },1200);


    }

    catch(error){

        hideLoader();

        console.error(error);

        showToast("Backend server is not running.",false);

    }

});