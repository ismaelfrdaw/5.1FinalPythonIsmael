import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("Testing API...")

    # 1. Create Author
    print("\n1. Creating Author...")
    author_data = {
        "name": "J.K. Rowling",
        "bio": "British author, best known for the Harry Potter series.",
        "birth_date": "1965-07-31",
        "nationality": "British"
    }
    response = requests.post(f"{BASE_URL}/authors/", json=author_data)
    if response.status_code == 201:
        author = response.json()
        print(f"Author created: {author}")
        author_id = author['id']
    else:
        print(f"Failed to create author: {response.text}")
        return

    # 2. Create Book
    print("\n2. Creating Book...")
    book_data = {
        "title": "Harry Potter and the Philosopher's Stone",
        "description": "The first novel in the Harry Potter series.",
        "publish_year": 1997,
        "pages": 223,
        "author_id": author_id
    }
    response = requests.post(f"{BASE_URL}/books/", json=book_data)
    if response.status_code == 201:
        book = response.json()
        print(f"Book created: {book}")
        book_id = book['id']
    else:
        print(f"Failed to create book: {response.text}")
        return

    # 3. Get Authors
    print("\n3. Getting Authors...")
    response = requests.get(f"{BASE_URL}/authors/")
    if response.status_code == 200:
        print(f"Authors: {response.json()}")
    else:
        print(f"Failed to get authors: {response.text}")

    # 4. Get Books
    print("\n4. Getting Books...")
    response = requests.get(f"{BASE_URL}/books/")
    if response.status_code == 200:
        print(f"Books: {response.json()}")
    else:
        print(f"Failed to get books: {response.text}")

    # 5. Get Author with Books
    print(f"\n5. Getting Author {author_id} with Books...")
    response = requests.get(f"{BASE_URL}/authors/{author_id}")
    if response.status_code == 200:
        print(f"Author with books: {response.json()}")
    else:
        print(f"Failed to get author: {response.text}")

    # 6. Update Book
    print(f"\n6. Updating Book {book_id}...")
    book_update_data = {
        "title": "Harry Potter and the Sorcerer's Stone",
        "description": "US Title",
        "publish_year": 1998,
        "pages": 309,
        "author_id": author_id
    }
    response = requests.put(f"{BASE_URL}/books/{book_id}", json=book_update_data)
    if response.status_code == 200:
        print(f"Book updated: {response.json()}")
    else:
        print(f"Failed to update book: {response.text}")

    # 7. Delete Book
    print(f"\n7. Deleting Book {book_id}...")
    response = requests.delete(f"{BASE_URL}/books/{book_id}")
    if response.status_code == 204:
        print("Book deleted successfully")
    else:
        print(f"Failed to delete book: {response.text}")

    # 8. Delete Author
    print(f"\n8. Deleting Author {author_id}...")
    response = requests.delete(f"{BASE_URL}/authors/{author_id}")
    if response.status_code == 204:
        print("Author deleted successfully")
    else:
        print(f"Failed to delete author: {response.text}")

if __name__ == "__main__":
    try:
        test_api()
    except Exception as e:
        print(f"An error occurred: {e}")
