// ======================================================
// SCHOOL PORTAL
// LOGIN.JS
// ======================================================

const API_URL = "http://127.0.0.1:8000";


// ======================================================
// ELEMENTS
// ======================================================

const loginForm = document.getElementById("loginForm");

const loader = document.getElementById("loader");

const toast = document.getElementById("toast");


// ======================================================
// AUTO REDIRECT
// ======================================================

let loggedUser = null;

try {

    const saved = localStorage.getItem("student");

    if (

        saved &&

        saved !== "undefined" &&

        saved !== "null"

    ) {

        loggedUser = JSON.parse(saved);

    }

}

catch {

    localStorage.removeItem("student");

}

if (loggedUser) {

    window.location.href = "index.html";

}

// ======================================================
// TOAST
// ======================================================

function showToast(message, success = true) {

    toast.textContent = message;

    toast.style.display = "block";

    toast.style.background = success
        ? "#16a34a"
        : "#dc2626";

    setTimeout(() => {

        toast.style.display = "none";

    }, 3000);

}


// ======================================================
// LOADER
// ======================================================

function showLoader() {

    loader.classList.remove("hidden");

}

function hideLoader() {

    loader.classList.add("hidden");

}


// ======================================================
// LOGIN
// ======================================================

loginForm.addEventListener("submit", async function (e) {

    e.preventDefault();

    const roll = Number(
        document.getElementById("roll").value
    );

    const password =
        document.getElementById("password").value.trim();

    // ===========================================
    // VALIDATION
    // ===========================================

    if (!roll || !password) {

        showToast("Please enter Roll Number and Password.", false);

        return;

    }

    showLoader();

    try {

        const response = await fetch(`${API_URL}/login`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                roll,
                password

            })

        });

        const data = await response.json();

        hideLoader();

        if (!response.ok) {

            showToast(data.detail || "Invalid credentials.", false);

            return;

        }

        // ===========================================
        // SAVE USER
        // ===========================================

        localStorage.setItem(

            "student",

            JSON.stringify(data.student)

        );

        showToast("Login Successful!");

        setTimeout(() => {

            window.location.href = "index.html";

        }, 1000);

    }

    catch (error) {

        hideLoader();

        console.error(error);

        showToast("Cannot connect to backend.", false);

    }

});
// ======================================================
// GO TO SIGNUP
// ======================================================

// const signupBtn = document.getElementById("signupBtn");

// if (signupBtn) {

//     signupBtn.addEventListener("click", () => {

//         window.location.href = "signup.html";

//     });

// }