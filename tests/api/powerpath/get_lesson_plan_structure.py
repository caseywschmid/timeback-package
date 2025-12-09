"""API test for get_lesson_plan_structure endpoint.

Usage:
    python -m tests.api.powerpath.get_lesson_plan_structure
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual lesson plan ID
    lesson_plan_id = "<lesson-plan-id>"

    print(f"Getting lesson plan structure: {lesson_plan_id}")
    print("-" * 60)

    response = client.powerpath.get_lesson_plan_structure(lesson_plan_id)

    data = response.lessonPlan.lessonPlan
    print(f"ID: {data.id}")
    print(f"Course: {data.courseTitle}")
    print(f"Structure nodes: {len(data.structure)}")
    print("-" * 60)

    for node in data.structure[:5]:  # Show first 5
        skip = "[SKIPPED] " if node.skipped else ""
        print(f"  {skip}[{node.type}] {node.title} (order: {node.order})")


if __name__ == "__main__":
    main()

