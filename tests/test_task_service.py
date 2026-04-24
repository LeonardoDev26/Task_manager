import unittest
from services.task_service import create_task, get_tasks

class TestTaskService(unittest.TestCase):
    def test_create_task(self):
        #crea tarea
        create_task("Test","Testing","2026")

        #obtener tareas
        tasks = get_tasks()

        #verificar que hay al menos una
        self.assertTrue(len(tasks) > 0)


if __name__ == "__main__":
    unittest.main()