import streamlit as st
import toml
import requests
# -----------------------

# load secrets.toml configuration
# secrets = st.connection('.streamlit/secrets.toml')

# Initialize connection
db_config = st.secrets['connections']['postgresql']


# conn = st.connection(
#     db_config['database'],
#     type='sql',
#     autocommit=True,
#     username=db_config["username"],
#     password=db_config["password"],
#     host=db_config["host"],
#     port=db_config["port"],
#     dialect=db_config["dialect"]
# )

conn = st.connection("postgresql", type="sql")


# Perform query
df = conn.query('SELECT * FROM products;', ttl="10m")


# for row in df.itertuples():
#     st.write(f"{row.name} with id: {row.id}")

st.title("Table Products")

# Display data in an iterative table
st.dataframe(df)

# Display data in a static table
# st.table(df)

# ------------------------

# Function to get a joke from the Chuck Norris API
def get_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['value']
    else:
        return "Sorry, I couldn't fetch a joke at this time."

# Streamlit app
st.title("Chuck Norris Joke Generator")

# Initialize session state for joke history
if 'joke_history' not in st.session_state:
    st.session_state.joke_history = []

# Custom CSS for the button
st.markdown(
    """
    <style>
    .red-button {
        background-color: red;
        color: white;
        border: None;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Button with custom class
if st.markdown('<button class="red-button" onclick="window.location.reload();">Get a Joke</button>', unsafe_allow_html=True):
    joke = get_joke()
    st.session_state.joke_history.append(joke)  # Store the joke in history

# Display the current joke
if st.session_state.joke_history:
    st.write("Latest Joke:")
    st.write(st.session_state.joke_history[-1])  # Show the latest joke

# Display joke history
if st.session_state.joke_history:
    st.write("Joke History:")
    for idx, joke in enumerate(st.session_state.joke_history):
        st.write(f"{idx + 1}: {joke}")
