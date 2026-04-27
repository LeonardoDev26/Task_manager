const API_URL = "http://127.0.0.1:8000";

async function loadTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);
        const tasks = await response.json();

        const list = document.getElementById("task-list");
        list.innerHTML = "";

        tasks.forEach(task => {
            const li = document.createElement("li");
            li.classList.add("task-item");

            li.innerHTML = `
                <div class="task-content">
                    <strong>${task[1]}</strong>
                    <p>${task[2] || ""}</p>
                    <small>${task[3] || ""}</small>
                </div>

                <div class="task-actions">
                    <button class="delete-btn" onclick="deleteTask(${task[0]})">
                        Eliminar
                    </button>

                    <button class="complete-btn" onclick="completeTask(${task[0]})">
                        Completar
                    </button>
                </div>
            `;

            list.appendChild(li);
        });

    } catch (error) {
        console.error("Error cargando tareas:", error);
    }
}

async function addTask() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const date = document.getElementById("date").value;

    if (!title) return;

    try {
        await fetch(`${API_URL}/tasks`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title,
                description,
                date
            })
        });

        // limpiar inputs
        document.getElementById("title").value = "";
        document.getElementById("description").value = "";
        document.getElementById("date").value = "";

        loadTasks();

    } catch (error) {
        console.error("Error creando tarea:", error);
    }
}

async function deleteTask(id) {
    try {
        await fetch(`${API_URL}/tasks/${id}`, {
            method: "DELETE"
        });

        loadTasks();

    } catch (error) {
        console.error("Error eliminando tarea:", error);
    }
}

async function completeTask(id) {
    try {
        await fetch(`${API_URL}/tasks/${id}/complete`, {
            method: "PUT"
        });

        loadTasks();

    } catch (error) {
        console.error("Error completando tarea:", error);
    }
}

window.onload = loadTasks;