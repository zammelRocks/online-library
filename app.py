import gradio as gr
import pandas as pd

# Sample book data - in a real application, this would come from a database
BOOKS = [
    {
        "Titre": "Pride and Prejudice",
        "Auteur": "Jane Austen",
        "Nb Page": "513",
        "Prix": "200",
    },
    {
        "Titre": "1984",
        "Auteur": "George Orwell",
        "Nb Page": "120",
        "Prix": "30",
    },
]


df = pd.DataFrame(BOOKS)


def read_book(title, db):
    """Returns the content of a selected book"""
    book = db[db["Titre"] == title].iloc[0].to_dict()
    out = ""
    for key, value in book.items():
        out += f"**{key}** : {value}\n\n"
    return out.strip()


def merge_with_db(db, new_db, book_input):
    new_db = pd.read_excel(new_db)
    new_db = new_db[["Titre", "Auteur", "Nb Page", "Prix"]]
    concatenated_db = pd.concat([db, new_db], ignore_index=True, axis=0)
    titles = list(concatenated_db["Titre"])
    return concatenated_db, gr.update(choices=titles, value=book_input)


# Create the Gradio interface
with gr.Blocks(title="Online Library") as demo:
    gr.Markdown("# Welcome to the Online Library")

    with gr.Tab("Browse Books"):
        new_db = gr.File(label="Upload a csv or an xlsx database of books")
        merge_with_db_button = gr.Button("Process database")
        db = gr.Dataframe(value=df, interactive=False, every=None)

    with gr.Tab("Read Book"):
        book_input = gr.Dropdown(
            choices=list(df["Titre"]),
            label="Select a book to read",
        )
        book_content = gr.Markdown(label="Book Content")
        book_input.change(fn=read_book, inputs=[book_input, db], outputs=[book_content])

    merge_with_db_button.click(
        fn=merge_with_db, inputs=[db, new_db, book_input], outputs=[db, book_input]
    )

if __name__ == "__main__":
    demo.launch()
