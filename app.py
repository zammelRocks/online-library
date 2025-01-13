import gradio as gr
import pandas as pd
from PIL import Image

# Sample book data - in a real application, this would come from a database
BOOKS = [
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "description": "A romantic novel of manners...",
        "content": "It is a truth universally acknowledged...",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "description": "A dystopian social science fiction novel...",
        "content": "It was a bright cold day in April...",
    },
]


def view_books():
    """Returns the list of available books"""
    books_df = pd.DataFrame(BOOKS)
    return books_df


def read_book(title):
    """Returns the content of a selected book"""
    for book in BOOKS:
        if book["title"] == title:
            return (
                f"Title: {book['title']}\nAuthor: {book['author']}\n\n{book['content']}"
            )
    return "Book not found"


# Create the Gradio interface
with gr.Blocks(title="Online Library") as demo:
    gr.Markdown("# Welcome to the Online Library")

    with gr.Tab("Browse Books"):
        gr.Dataframe(value=view_books, interactive=False, every=None)

    with gr.Tab("Read Book"):
        book_input = gr.Dropdown(
            choices=[book["title"] for book in BOOKS], label="Select a book to read"
        )
        book_content = gr.TextArea(label="Book Content", interactive=False)
        book_input.change(fn=read_book, inputs=[book_input], outputs=[book_content])

if __name__ == "__main__":
    demo.launch()
