import { useState } from "react";

function App() {
    const [longurl, setLongurl] = useState("");
    const [shorturl, setShorturl] = useState("");
    const [returnLongURL, setReturnLongURL] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch("http://127.0.0.1:8000/api/create/", {
            method: "POST",
            body: JSON.stringify({ longurl: longurl }),
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
                setShorturl(data.shorturl);
                setReturnLongURL(data.longurl);
                setLongurl("");
            });
    };

    return (
        <>
        <div className="w-full pt-20 bg-gray-200 min-h-screen">
          <h2 className="text-green-500 text-center text-4xl font-semibold mb-10">
            URL Shortener
          </h2>

          <div className="flex items-center justify-center">
            <div className="w-8/12 flex flex-col justify-center items-center px-10">
                <form className="w-full mb-10">
                  <input
                    className="w-full p-2 placeholder-gray-500 block outline-none bg-gray-100 rounded-lg shadow-lg my-4"
                    placeholder="Paste your long URL here ..."
                    type="text"
                    name="longurl"
                    value={longurl}
                    onChange={(e) => setLongurl(e.target.value)} />
                
                  <button
                    className="block py-2 bg-blue-500 w-full focus:outline-none rounded-lg shadow-md text-gray-100 font-semibold"
                    type="submit"
                    onClick={(e) => handleSubmit(e)}
                    disabled={!longurl}
                  >
                    Shorten it!
                  </button>
                </form>
                <div>
                  <p>Long URL: {returnLongURL}</p>
                  <p
                    style={{ cursor: "pointer" }}
                    onClick={() => window.open(returnLongURL)}
                  >
                    Short URL: {shorturl}
                  </p>
                </div>
            </div>
            <div className="w-2/12 flex justify-center items-center">
              <img src="assets/undraw_link_shortener_mvf6.svg"></img>
            </div>
            <div></div>
          </div>
        </div>
      </>
    );
}

export default App;