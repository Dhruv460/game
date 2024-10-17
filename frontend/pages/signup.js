import { useState } from "react";

export default function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const signupData = {
      name,
      email,
      password,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/api/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(signupData),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage("Signup successful!");
      } else {
        setMessage(data.error || "Signup failed");
      }
    } catch (error) {
      setMessage("Error connecting to the API");
    }
  };

  return (
    <div>
      <h1>Signup Form</h1>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <br />

        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <br />

        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <br />

        <button type="submit">Sign Up</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}
