import unittest
from services.task_service import create_task, get_tasks, delete_task, complete_task
from database.models import create_tables


class TestTaskService(unittest.TestCase):

    def setUp(self):
        # Crear tabla antes de cada test
        create_tables()

    def test_create_task(self):
        create_task("Test", "Testing", "2026-01-01")
        tasks = get_tasks()

        self.assertTrue(len(tasks) > 0)
        self.assertEqual(tasks[-1][1], "Test")

    def test_delete_task(self):
        create_task("Eliminar", "Test delete", "2026-01-01")
        tasks = get_tasks()
        task_id = tasks[-1][0]

        delete_task(task_id)
        tasks = get_tasks()

        ids = [task[0] for task in tasks]
        self.assertNotIn(task_id, ids)

    def test_complete_task(self):
        create_task("Completar", "Test complete", "2026-01-01")
        tasks = get_tasks()
        task_id = tasks[-1][0]

        complete_task(task_id)
        tasks = get_tasks()

        for task in tasks:
            if task[0] == task_id:
                self.assertEqual(task[4], 1)


if __name__ == "__main__":
    unittest.main()