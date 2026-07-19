// ======================================================
// School Portal Dashboard
// script.js (Part 1)
// Backend: FastAPI (Unchanged)
// ======================================================

// ======================================================
// CONFIGURATION
// ======================================================
const API_URL = "http://127.0.0.1:8000";

// ======================================================
// DOM ELEMENTS
// =====================================================
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

// ======================================================
// GLOBAL VARIABLES
// ======================================================
let deleteRoll = null;

// ======================================================
// API REQUEST
// ======================================================
async function apiRequest(url, options = {}) {
    const response = await fetch(url, options);
    const data = await response.json();
    if (!response.ok) {
        throw new Error(
            data.detail || "Something went wrong."
        );
    }
    return data;
}

// ======================================================
// TOAST
// ======================================================
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
    }, 4000);
}

// ======================================================
// LOADER
// ======================================================
function showLoader() {
    if (!loader) return;
    loader.classList.remove("hidden");
}
function hideLoader() {
    if (!loader) return;
    loader.classList.add("hidden");
}

// ======================================================
// BUTTON STATES
// ======================================================
function disableButtons() {
    addStudentBtn.disabled = true;
    addCourseBtn.disabled = true;
    refreshBtn.disabled = true;
}

function enableButtons() {
    addStudentBtn.disabled = false;
    addCourseBtn.disabled = false;
    refreshBtn.disabled = false;
}

// ======================================================
// MODAL
// ======================================================
function openDeleteModal(roll) {
    deleteRoll = roll;
    if (!modal) {
        deleteStudent(roll);
        return;
    }
    modal.classList.remove("hidden");
}

function closeDeleteModal() {
    deleteRoll = null;
    modal.classList.add("hidden");
}

// ======================================================
// ADD STUDENT
// ======================================================
async function addStudent() {
    const student = {
        roll: Number(rollInput.value),
        name: nameInput.value.trim()
    };
    if (!student.roll || student.name === "") {
        showToast(
            "Please fill all student details.",
            "error"
        );
        return;
    }
    disableButtons();
    showLoader();
    try {
        await apiRequest(
            `${API_URL}/students`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(student)
            }
        );
        showToast(
            "Student enrolled successfully!"
        );
        rollInput.value = "";
        nameInput.value = "";
        loadStudents();
    }
    catch (error) {
        console.error(error);
        showToast(error.message, "error");
    }
    finally {
        hideLoader();
        enableButtons();
    }
}

// ======================================================
// ADD COURSE
// ======================================================
async function addCourse() {
    const roll = Number(courseRollInput.value);
    const course = {
        title: courseTitleInput.value.trim()
    };
    if (!roll || course.title === "") {
        showToast(
            "Please fill all course details.",
            "error"
        );
        return;
    }
    disableButtons();
    showLoader();
    try {
        await apiRequest(
            `${API_URL}/students/${roll}/courses`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(course)
            }
        );
        showToast(
            "Course assigned successfully!"
        );
        courseRollInput.value = "";
        courseTitleInput.value = "";
        loadStudents();
    }
    catch (error) {
        console.error(error);
        showToast(error.message, "error");
    }
    finally {
        hideLoader();
        enableButtons();
    }
}

// ======================================================
// DELETE STUDENT
// ======================================================

async function deleteStudent(roll = deleteRoll) {
    if (!roll) return;
    closeDeleteModal();
    disableButtons();
    showLoader();
    try {
        const data = await apiRequest(
            `${API_URL}/students/${roll}`,
            {
                method: "DELETE"
            }
        );
        showToast(data.message);
        loadStudents();
    }
    catch (error) {
        console.error(error);
        showToast(error.message, "error");
    }
    finally {
        hideLoader();
        enableButtons();
    }

}
// ======================================================
// LOAD STUDENTS
// ======================================================
async function loadStudents() {
    showLoader();
    refreshBtn.classList.add("spin");
    try {
        const students = await apiRequest(
            `${API_URL}/students`
        );
        renderStudents(students);
        updateDashboard(students);
    }
    catch (error) {
        console.error(error);
        showToast(error.message, "error");
    }
    finally {
        hideLoader();
        refreshBtn.classList.remove("spin");
    }
}

// ======================================================
// RENDER TABLE
// ======================================================
function renderStudents(students) {
    studentTable.innerHTML = "";
    if (students.length === 0) {
        studentTable.innerHTML = `
        <tr>
            <td colspan="4">
                <div class="emptyState">
                    <div class="emptyIcon">
                        📚
                    </div>
                    <h3>
                        No Students Found
                    </h3>
                    <p>
                        Add your first student.
                    </p>
                </div>
            </td>
        </tr>
        `;
        return;
    }

    let rows = "";
    students.forEach((student, index) => {
        const courses = student.courses
            .map(course => course.title)
            .join(", ");
        const avatarLetter =
            student.name.charAt(0).toUpperCase();
        rows += `
        <tr
            class="fadeRow"
            style="animation-delay:${index * 0.08}s">
            <td>
                <div class="studentInfo">
                    <div class="avatar">
                        ${avatarLetter}
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
                ${
                    courses
                    ||
                    "<span class='courseEmpty'>No Courses</span>"
                }
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
    studentTable.innerHTML = rows;
}

// ======================================================
// UPDATE DASHBOARD
// ======================================================
function updateDashboard(students) {
    if (studentCount) {
        studentCount.textContent =
            students.length;
    }
    let totalCourses = 0;
    students.forEach(student => {
        totalCourses += student.courses.length;
    });
    if (courseCount) {
        courseCount.textContent =
            totalCourses;
    }
}


// ======================================================
// ENTER KEY SUPPORT
// ======================================================
nameInput.addEventListener(
    "keydown",
    function (e) {
        if (e.key === "Enter") {
            addStudent();
        }
    }
);
courseTitleInput.addEventListener(
    "keydown",
    function (e) {
        if (e.key === "Enter") {
            addCourse();
        }
    }
);

// ======================================================
// MODAL EVENTS
// ======================================================
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

// ======================================================
// CLOSE MODAL WHEN CLICKING OUTSIDE
// ======================================================
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

// ======================================================
// BUTTON EVENTS
// ======================================================
addStudentBtn.addEventListener(
    "click",
    addStudent
);
addCourseBtn.addEventListener(
    "click",
    addCourse
);
refreshBtn.addEventListener(
    "click",
    loadStudents
);

// ======================================================
// INITIAL LOAD
// ======================================================
document.addEventListener(
    "DOMContentLoaded",
    () => {
        loadStudents();

    }
);

// ======================================================
// END OF SCRIPT
// ======================================================