// ==========================================================
// School Portal
// signup.js
// ==========================================================

const API_URL = "http://127.0.0.1:8000";

// ==========================================================
// DOM
// ==========================================================

const rollInput = document.getElementById("roll");
const passwordInput = document.getElementById("password");
const confirmInput = document.getElementById("confirmPassword");

const signupBtn = document.getElementById("signupBtn");

const toast = document.getElementById("toast");
const loader = document.getElementById("loader");

// ==========================================================
// Helpers
// ==========================================================

function showToast(message, type = "success") {

    if (!toast) {
        alert(message);
        return;
    }

    toast.innerText = message;

    toast.className = "toast";

    toast.classList.add(type);

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 3000);

}

function showLoader() {

    if (loader)
        loader.classList.remove("hidden");

}

function hideLoader() {

    if (loader)
        loader.classList.add("hidden");

}

// ==========================================================
// Signup
// ==========================================================

async function createAccount() {

    console.clear();

    console.log("Signup Started");

    const roll = rollInput.value.trim();

    const password = passwordInput.value.trim();

    const confirm = confirmInput.value.trim();

    // -----------------------------
    // Validation
    // -----------------------------

    if (roll === "") {

        showToast("Enter Roll Number", "error");

        return;

    }

    if (password === "") {

        showToast("Enter Password", "error");

        return;

    }

    if (confirm === "") {

        showToast("Confirm Password", "error");

        return;

    }

    if (password !== confirm) {

        showToast("Passwords do not match", "error");

        return;

    }

    signupBtn.disabled = true;

    showLoader();

    try {

        console.log("Sending Request...");

        const response = await fetch(`${API_URL}/signup`, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                roll: Number(roll),

                password: password

            })

        });

        const data = await response.json();

        console.log(data);

        if (!response.ok) {

            throw new Error(data.detail || "Signup Failed");

        }

        // -----------------------------
        // Save Login
        // -----------------------------

        localStorage.setItem(

            "user_id",

            data.id

        );

        localStorage.setItem(

            "roll",

            data.roll

        );

        localStorage.setItem(

            "currentUser",

            JSON.stringify(data)

        );

        showToast("Account Created Successfully");

        console.log("Redirecting...");

        setTimeout(() => {

            window.location.href = "index.html";

        }, 1200);

    }

    catch (err) {

        console.error(err);

        showToast(err.message, "error");

    }

    finally {

        signupBtn.disabled = false;

        hideLoader();

    }

}

// ==========================================================
// Events
// ==========================================================

signupBtn.addEventListener(

    "click",

    function (e) {

        e.preventDefault();

        createAccount();

    }

);

document.addEventListener(

    "keydown",

    function (e) {

        if (e.key === "Enter") {

            createAccount();

        }

    }

);

console.log("signup.js Loaded Successfully");