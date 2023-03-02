import asyncio

from temporalio.client import Client

from your_workflows import YourWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        YourWorkflow.run, "my name", id="my-workflow-id", task_queue="my-task-queue"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
