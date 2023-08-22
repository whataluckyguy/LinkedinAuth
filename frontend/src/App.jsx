import "./App.css";
import axios from "axios";
import { LinkedInApi } from "./Config";
import { useEffect, useState } from "react";

function App() {
  const { redirectUrl, clientId, oauthUrl, scope, state } = LinkedInApi;
  const [code, setCode] = useState(null);

  useEffect(() => {
    const URL = window.location.href;
    const hasCode = URL.includes("?code=");
    if (hasCode) {
      const newCode = URL.split("?code=")[1];
      setCode(newCode);
    }
  }, []);

  useEffect(() => {
    if (code !== null) {
      axios
        .get(`http://localhost:5000/auth?code=${code}`)
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }, [code]);

  const getUserCreds = async (cod) => {
    if (cod !== null) {
      axios
        .get(`http://localhost:5000/auth?code=${cod}`)
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  };

  return (
    <>
      <h1>Linkedin Authentication</h1>
      <a
        href={`${oauthUrl}&client_id=${clientId}&scope=${scope}&state=${state}&redirect_uri=${redirectUrl}`}
      >
        Click here to authenticate
      </a>
    </>
  );
}

export default App;
