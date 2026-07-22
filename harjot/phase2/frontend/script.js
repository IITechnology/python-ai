// ==========================================================
// School Portal Dashboard
// script.js
// PART 1 OF 3
// ==========================================================

// ==========================================================
// CONFIGURATION
// ==========================================================

const API_URL = "http://127.0.0.1:8000";

// ==========================================================
// AUTHENTICATION
// ==========================================================

// Signup saves:
// localStorage.setItem("user_id", data.id);
// localStorage.setItem("roll", data.roll);

const userId = localStorage.getItem("user_id");

if (!userId) {
    window.location.replace("signup.html");
}

// ==========================================================
// DOM ELEMENTS
// ==========================================================

const rollInput = document.getElementById("roll");
const nameInput = document.getElementById("name");

const courseRollInput = document.getElementById("courseRoll");
const courseTitleInput = document.getElementById("courseTitle");

const addStudentBtn = document.getElementById("addStudentBtn");
const addCourseBtn = document.getElementById("addCourseBtn");
const refreshBtn = document.getElementById("refreshBtn");

const studentTable = document.getElementById("studentTable");

const studentCount = document.getElementById("studentCount");
const courseCount = document.getElementById("courseCount");

const toast = document.getElementById("toast");
const loader = document.getElementById("loader");

const modal = document.getElementById("modal");
const confirmDeleteBtn = document.getElementById("confirmDelete");
const cancelDeleteBtn = document.getElementById("cancelDelete");

// ==========================================================
// GLOBAL VARIABLES
// ==========================================================

let deleteRoll = null;

// ==========================================================
// TOAST
// ==========================================================

function showToast(message, type = "success") {

    if (!toast) {
        alert(message);
        return;
    }

    toast.textContent = message;

    toast.className = "toast";

    toast.classList.add(type);

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 3000);

}

// ==========================================================
// LOADER
// ==========================================================

function showLoader() {

    if (loader) {

        loader.classList.remove("hidden");

    }

}

function hideLoader() {

    if (loader) {

        loader.classList.add("hidden");

    }

}

// ==========================================================
// API REQUEST HELPER
// ==========================================================

async function apiRequest(endpoint, options = {}) {

    const response = await fetch(API_URL + endpoint, options);

    let data = {};

    try {

        data = await response.json();

    } catch (e) {

        data = {};

    }

    if (!response.ok) {

        throw new Error(data.detail || "Request Failed");

    }

    return data;

}

// ==========================================================
// DELETE MODAL
// ==========================================================

function openDeleteModal(roll) {

    deleteRoll = roll;

    if (modal) {

        modal.classList.remove("hidden");

    }

}

function closeDeleteModal() {

    deleteRoll = null;

    if (modal) {

        modal.classList.add("hidden");

    }

}

// ==========================================================
// DASHBOARD LOADER
// ==========================================================

async function loadStudents() {

    showLoader();

    try {

        const students = await apiRequest("/students");

        renderStudents(students);

        updateDashboard(students);

    }

    catch (err) {

        console.error(err);

        showToast(err.message, "error");

    }

    finally {

        hideLoader();

    }

}

// ==========================================================
// PART 2 STARTS FROM addStudent()
// ==========================================================
// ==========================================================
// School Portal Dashboard
// script.js
// PART 2 OF 3
// ==========================================================

// ==========================================================
// ADD STUDENT
// ==========================================================

async function addStudent() {

    const roll = Number(rollInput.value);

    const name = nameInput.value.trim();

    if (!roll || name === "") {

        showToast("Please enter Roll Number and Student Name.", "error");

        return;

    }

    showLoader();

    addStudentBtn.disabled = true;

    try {

        await apiRequest("/students", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                roll: roll,

                name: name

            })

        });

        showToast("Student enrolled successfully.");

        rollInput.value = "";

        nameInput.value = "";

        await loadStudents();

    }

    catch (err) {

        console.error(err);

        showToast(err.message, "error");

    }

    finally {

        hideLoader();

        addStudentBtn.disabled = false;

    }

}


// ==========================================================
// ADD COURSE
// ==========================================================

async function addCourse() {

    const roll = Number(courseRollInput.value);

    const title = courseTitleInput.value.trim();

    if (!roll || title === "") {

        showToast("Please enter Roll Number and Course Title.", "error");

        return;

    }

    showLoader();

    addCourseBtn.disabled = true;

    try {

        await apiRequest(`/students/${roll}/courses`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                title: title

            })

        });

        showToast("Course assigned successfully.");

        courseRollInput.value = "";

        courseTitleInput.value = "";

        await loadStudents();

    }

    catch (err) {

        console.error(err);

        showToast(err.message, "error");

    }

    finally {

        hideLoader();

        addCourseBtn.disabled = false;

    }

}


// ==========================================================
// DELETE STUDENT
// ==========================================================

async function deleteStudent() {

    if (deleteRoll === null) {

        return;

    }

    showLoader();

    try {

        const result = await apiRequest(`/students/${deleteRoll}`, {

            method: "DELETE"

        });

        showToast(result.message);

        closeDeleteModal();

        await loadStudents();

    }

    catch (err) {

        console.error(err);

        showToast(err.message, "error");

    }

    finally {

        hideLoader();

    }

}


// ==========================================================
// REFRESH DASHBOARD
// ==========================================================

async function refreshDashboard() {

    await loadStudents();

    showToast("Dashboard refreshed.");

}


// ==========================================================
// MODAL EVENTS
// ==========================================================

if (confirmDeleteBtn) {

    confirmDeleteBtn.addEventListener(

        "click",

        deleteStudent

    );

}

if (cancelDeleteBtn) {

    cancelDeleteBtn.addEventListener(

        "click",

        closeDeleteModal

    );

}

if (modal) {

    modal.addEventListener(

        "click",

        function (e) {

            if (e.target === modal) {

                closeDeleteModal();

            }

        }

    );

}


// ==========================================================
// BUTTON EVENTS
// ==========================================================

if (addStudentBtn) {

    addStudentBtn.addEventListener(

        "click",

        addStudent

    );

}

if (addCourseBtn) {

    addCourseBtn.addEventListener(

        "click",

        addCourse

    );

}

if (refreshBtn) {

    refreshBtn.addEventListener(

        "click",

        refreshDashboard

    );

}


// ==========================================================
// ENTER KEY SUPPORT
// ==========================================================

if (nameInput) {

    nameInput.addEventListener(

        "keydown",

        function (e) {

            if (e.key === "Enter") {

                addStudent();

            }

        }

    );

}

if (courseTitleInput) {

    courseTitleInput.addEventListener(

        "keydown",

        function (e) {

            if (e.key === "Enter") {

                addCourse();

            }

        }

    );

}

// ==========================================================
// PART 3 STARTS WITH renderStudents()
// ==========================================================
// ======================================================
// School Portal Dashboard
// script.js
// PART 3 / 3
// ======================================================

// ======================================================
// RENDER STUDENTS TABLE
// ======================================================

function renderStudents(students) {

    if (!studentTable) return;

    studentTable.innerHTML = "";

    if (students.length === 0) {

        studentTable.innerHTML = `
            <tr>
                <td colspan="4">
                    <div class="emptyState">

                        <div class="emptyIcon">
                            📚
                        </div>

                        <h3>No Students Found</h3>

                        <p>Add your first student.</p>

                    </div>
                </td>
            </tr>
        `;

        return;

    }

    let html = "";

    students.forEach((student, index) => {

        const courses = student.courses
            .map(course => course.title)
            .join(", ");

        html += `

        <tr
            class="fadeRow"
            style="animation-delay:${index * 0.08}s">

            <td>

                <div class="studentInfo">

                    <div class="avatar">

                        ${student.name.charAt(0).toUpperCase()}

                    </div>

                    <span>

                        ${student.name}

                    </span>

                </div>

            </td>

            <td>

                ${student.roll}

            </td>

            <td>

                ${courses || "<span class='courseEmpty'>No Courses</span>"}

            </td>

            <td>

                <button
                    class="deleteBtn"
                    onclick="openDeleteModal(${student.roll})">

                    🗑 Delete

                </button>

            </td>

        </tr>

        `;

    });

    studentTable.innerHTML = html;

}


// ======================================================
// UPDATE DASHBOARD
// ======================================================

function updateDashboard(students) {

    if (studentCount) {

        studentCount.textContent = students.length;

    }

    let totalCourses = 0;

    students.forEach(student => {

        totalCourses += student.courses.length;

    });

    if (courseCount) {

        courseCount.textContent = totalCourses;

    }

}


// ======================================================
// EVENTS
// ======================================================

if (addStudentBtn) {

    addStudentBtn.addEventListener(

        "click",

        addStudent

    );

}

if (addCourseBtn) {

    addCourseBtn.addEventListener(

        "click",

        addCourse

    );

}

if (refreshBtn) {

    refreshBtn.addEventListener(

        "click",

        refreshDashboard

    );

}

if (confirmDeleteBtn) {

    confirmDeleteBtn.addEventListener(

        "click",

        () => deleteStudent()

    );

}

if (cancelDeleteBtn) {

    cancelDeleteBtn.addEventListener(

        "click",

        closeDeleteModal

    );

}

if (modal) {

    modal.addEventListener(

        "click",

        (e) => {

            if (e.target === modal) {

                closeDeleteModal();

            }

        }

    );

}


// ======================================================
// ENTER KEY SUPPORT
// ======================================================

if (nameInput) {

    nameInput.addEventListener(

        "keydown",

        function (e) {

            if (e.key === "Enter") {

                addStudent();

            }

        }

    );

}

if (courseTitleInput) {

    courseTitleInput.addEventListener(

        "keydown",

        function (e) {

            if (e.key === "Enter") {

                addCourse();

            }

        }

    );

}


// ======================================================
// PAGE LOAD
// ======================================================

document.addEventListener(

    "DOMContentLoaded",

    async () => {

        const currentUser = JSON.parse(

            localStorage.getItem("currentUser")

        );

        if (!currentUser) {

            window.location.replace("signup.html");

            return;

        }

        await loadStudents();

    }

);


// ======================================================
// END OF FILE
// ======================================================