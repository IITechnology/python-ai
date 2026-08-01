// ======================================================
// SCHOOL PORTAL
// SCRIPT.JS
// PART 1
// Configuration • DOM • Authentication • Helpers • API
// ======================================================

// ======================================================
// CONFIGURATION
// ======================================================

const API_URL = "http://127.0.0.1:8000";

// ======================================================
// DOM ELEMENTS
// ======================================================

// Header

const logoutBtn = document.getElementById("logoutBtn");

// Welcome

const studentName = document.getElementById("studentName");

// Dashboard

const studentCount = document.getElementById("studentCount");
const courseCount = document.getElementById("courseCount");

// Course

const courseForm = document.getElementById("courseForm");
const courseRoll = document.getElementById("courseRoll");
const courseInput = document.getElementById("course");

// Table

const studentTableBody = document.getElementById("studentTableBody");
const refreshBtn = document.getElementById("refreshBtn");
const emptyState = document.getElementById("emptyState");

// Modal

const editModal = document.getElementById("editModal");
const updateForm = document.getElementById("updateForm");

const updateRoll = document.getElementById("updateRoll");
const updateName = document.getElementById("updateName");
const updateEmail = document.getElementById("updateEmail");
const updateBranch = document.getElementById("updateBranch");
const updateSemester = document.getElementById("updateSemester");

const closeModal = document.getElementById("closeModal");
const cancelBtn = document.getElementById("cancelBtn");

// Utilities

const loader = document.getElementById("loader");
const toast = document.getElementById("toast");

// ======================================================
// GLOBAL STATE
// ======================================================

let students = [];
let currentStudent = null;
let editingRoll = null;

// ======================================================
// AUTHENTICATION
// ======================================================

function checkAuthentication() {

    const stored = localStorage.getItem("student");

    if (!stored) {

        window.location.href = "login.html";
        return false;

    }

    try {

        currentStudent = JSON.parse(stored);

    }

    catch (error) {

        console.error(error);

        localStorage.removeItem("student");

        window.location.href = "login.html";

        return false;

    }

    return true;

}

// ======================================================
// INITIALIZE CURRENT USER
// ======================================================

function initializeCurrentStudent() {

    if (!currentStudent) {

        return;

    }

    studentName.textContent = currentStudent.name;

    courseRoll.value = currentStudent.roll;

}

// ======================================================
// LOGOUT
// ======================================================

function logout() {

    localStorage.removeItem("student");

    window.location.href = "login.html";

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
// TOAST
// ======================================================

function showToast(message, success = true) {

    toast.textContent = message;

    toast.style.background =
        success
            ? "#16a34a"
            : "#dc2626";

    toast.classList.remove("hidden");

    setTimeout(() => {

        toast.classList.add("hidden");

    }, 2500);

}

// ======================================================
// MODAL
// ======================================================

function openModal() {

    editModal.classList.remove("hidden");

}

function closeEditModal() {

    editModal.classList.add("hidden");

    updateForm.reset();

    editingRoll = null;

}

// ======================================================
// API
// GET STUDENTS
// ======================================================

async function fetchStudents() {

    const response = await fetch(`${API_URL}/students`);

    if (!response.ok) {

        throw new Error("Unable to load students.");

    }

    return await response.json();

}

// ======================================================
// API
// ADD COURSE
// ======================================================

async function apiAddCourse(roll, title) {

    const response = await fetch(

        `${API_URL}/students/${roll}/courses`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                title

            })

        }

    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(data.detail);

    }

    return data;

}

// ======================================================
// API
// UPDATE STUDENT
// ======================================================

async function apiUpdateStudent(roll, payload) {

    const response = await fetch(

        `${API_URL}/students/${roll}`,

        {

            method: "PUT",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(payload)

        }

    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(data.detail);

    }

    return data;

}

// ======================================================
// API
// DELETE STUDENT
// ======================================================

async function apiDeleteStudent(roll) {

    const response = await fetch(

        `${API_URL}/students/${roll}`,

        {

            method: "DELETE"

        }

    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(data.detail);

    }

    return data;

}

// ======================================================
// LOAD STUDENTS
// ======================================================

async function loadStudents() {

    showLoader();

    try {

        students = await fetchStudents();

    }

    catch (error) {

        console.error(error);

        showToast(error.message, false);

    }

    finally {

        hideLoader();

    }

}
// ======================================================
// SCHOOL PORTAL
// SCRIPT.JS
// PART 2
// Rendering • Dashboard • CRUD
// ======================================================

// ======================================================
// COURSE BADGES
// ======================================================

function renderCourses(courses) {

    if (!courses || courses.length === 0) {

        return `<span class="noCourse">No Courses</span>`;

    }

    return courses.map(course =>

        `<span class="course">${course.title}</span>`

    ).join("");

}

// ======================================================
// DASHBOARD CARDS
// ======================================================

function renderDashboardCards() {

    studentCount.textContent = students.length;

    let totalCourses = 0;

    students.forEach(student => {

        totalCourses += student.courses.length;

    });

    courseCount.textContent = totalCourses;

}

// ======================================================
// STUDENT TABLE
// ======================================================

function renderStudentTable() {

    studentTableBody.innerHTML = "";

    if (students.length === 0) {

        emptyState.classList.remove("hidden");

        return;

    }

    emptyState.classList.add("hidden");

    students.forEach(student => {

        studentTableBody.innerHTML += `

        <tr>

            <td>${student.id}</td>

            <td>${student.roll}</td>

            <td>${student.name}</td>

            <td>${student.email}</td>

            <td>${student.branch}</td>

            <td>${student.semester}</td>

            <td>${renderCourses(student.courses)}</td>

            <td>

                <button
                    class="editBtn"
                    onclick="openEditModal(${student.roll})">

                    Edit

                </button>

                <button
                    class="deleteBtn"
                    onclick="deleteStudent(${student.roll})">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

}

// ======================================================
// RENDER COMPLETE DASHBOARD
// ======================================================

function renderDashboard() {

    renderDashboardCards();

    renderStudentTable();

}

// ======================================================
// REFRESH DASHBOARD
// ======================================================

async function refreshDashboard() {

    await loadStudents();

    renderDashboard();

}

// ======================================================
// ADD COURSE
// ======================================================

async function handleAddCourse(event) {

    event.preventDefault();

    const title = courseInput.value.trim();

    if (!title) {

        showToast(

            "Please enter course title.",

            false

        );

        return;

    }

    try {

        showLoader();

        await apiAddCourse(

            currentStudent.roll,

            title

        );

        courseInput.value = "";

        await refreshDashboard();

        showToast(

            "Course added successfully."

        );

    }

    catch (error) {

        console.error(error);

        showToast(

            error.message,

            false

        );

    }

    finally {

        hideLoader();

    }

}

// ======================================================
// OPEN EDIT MODAL
// ======================================================

function openEditModal(roll) {

    const student = students.find(

        s => s.roll === roll

    );

    if (!student) {

        return;

    }

    editingRoll = roll;

    updateRoll.value = student.roll;

    updateName.value = student.name;

    updateEmail.value = student.email;

    updateBranch.value = student.branch;

    updateSemester.value = student.semester;

    openModal();

}

// ======================================================
// UPDATE STUDENT
// ======================================================

async function handleUpdateStudent(event) {

    event.preventDefault();

    const payload = {

        name: updateName.value.trim(),

        email: updateEmail.value.trim(),

        branch: updateBranch.value,

        semester: Number(updateSemester.value)

    };

    try {

        showLoader();

        await apiUpdateStudent(

            editingRoll,

            payload

        );

        if (

            editingRoll ===

            currentStudent.roll

        ) {

            currentStudent = {

                ...currentStudent,

                ...payload

            };

            localStorage.setItem(

                "student",

                JSON.stringify(currentStudent)

            );

            initializeCurrentStudent();

        }

        closeEditModal();

        await refreshDashboard();

        showToast(

            "Student updated successfully."

        );

    }

    catch (error) {

        console.error(error);

        showToast(

            error.message,

            false

        );

    }

    finally {

        hideLoader();

    }

}

// ======================================================
// DELETE STUDENT
// ======================================================

async function deleteStudent(roll) {

    const confirmed = confirm(

        "Delete this student?"

    );

    if (!confirmed) {

        return;

    }

    try {

        showLoader();

        await apiDeleteStudent(roll);

        if (

            roll === currentStudent.roll

        ) {

            logout();

            return;

        }

        await refreshDashboard();

        showToast(

            "Student deleted."

        );

    }

    catch (error) {

        console.error(error);

        showToast(

            error.message,

            false

        );

    }

    finally {

        hideLoader();

    }

}
// ======================================================
// SCHOOL PORTAL
// SCRIPT.JS
// PART 3
// Events • Initialization • Start Application
// ======================================================

// ======================================================
// COURSE FORM
// ======================================================

courseForm.addEventListener(

    "submit",

    handleAddCourse

);

// ======================================================
// UPDATE FORM
// ======================================================

updateForm.addEventListener(

    "submit",

    handleUpdateStudent

);

// ======================================================
// REFRESH BUTTON
// ======================================================

refreshBtn.addEventListener(

    "click",

    async () => {

        try {

            await refreshDashboard();

            showToast(

                "Dashboard refreshed."

            );

        }

        catch (error) {

            console.error(error);

            showToast(

                "Unable to refresh dashboard.",

                false

            );

        }

    }

);

// ======================================================
// LOGOUT
// ======================================================

logoutBtn.addEventListener(

    "click",

    () => {

        const confirmLogout = confirm(

            "Do you want to logout?"

        );

        if (!confirmLogout) {

            return;

        }

        logout();

    }

);

// ======================================================
// MODAL EVENTS
// ======================================================

closeModal.addEventListener(

    "click",

    closeEditModal

);

cancelBtn.addEventListener(

    "click",

    closeEditModal

);

window.addEventListener(

    "click",

    event => {

        if (

            event.target === editModal

        ) {

            closeEditModal();

        }

    }

);

window.addEventListener(

    "keydown",

    event => {

        if (

            event.key === "Escape" &&

            !editModal.classList.contains("hidden")

        ) {

            closeEditModal();

        }

    }

);

// ======================================================
// INITIALIZE APPLICATION
// ======================================================

async function initializeApp() {

    const authenticated = checkAuthentication();

    if (!authenticated) {

        return;

    }

    initializeCurrentStudent();

    await refreshDashboard();

}

// ======================================================
// START APPLICATION
// ======================================================

document.addEventListener(

    "DOMContentLoaded",

    async () => {

        try {

            showLoader();

            await initializeApp();

        }

        catch (error) {

            console.error(error);

            showToast(

                "Unable to load dashboard.",

                false

            );

        }

        finally {

            hideLoader();

        }

    }

);

// ======================================================
// DEBUG
// ======================================================

console.log("====================================");
console.log("School Portal Dashboard Started");
console.log("API :", API_URL);
console.log("====================================");