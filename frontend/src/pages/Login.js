import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Login = ({ setUser }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    // Vetëm një shembull login
    if (username === 'admin' && password === 'admin') {
      setUser(username);
      navigate('/dashboard');
    } else {
      setError('Invalid username or password');
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.box}>
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <input
            style={styles.input}
            type="text"
            placeholder="Username"
            value={username}
            onChange={e => setUsername(e.target.value)}
            required
          />
          <input
            style={styles.input}
            type="password"
            placeholder="Password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
          />
          <button style={styles.button} type="submit">Login</button>
        </form>
        {error && <p style={{ color: 'red', marginTop: 10 }}>{error}</p>}
        <p style={{ marginTop: 15 }}>
          Don't have an account? <Link to="/register">Register here</Link>
        </p>
      </div>
    </div>
  );
};

const styles = {
  container: {
    height: '100vh',
    background: `url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1470&q=80') no-repeat center center fixed`,
    backgroundSize: 'cover',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
  box: {
    backgroundColor: 'rgba(255,255,255,0.9)',
    padding: 40,
    borderRadius: 15,
    width: '100%',
    maxWidth: 400,
    boxShadow: '0 10px 20px rgba(0,0,0,0.1)',
    textAlign: 'center',
  },
  input: {
    width: '100%',
    padding: 12,
    marginBottom: 20,
    fontSize: 16,
    borderRadius: 8,
    border: '2px solid #ccc',
  },
  button: {
    width: '100%',
    padding: 14,
    backgroundColor: '#2C3E50',
    color: 'white',
    fontWeight: '600',
    fontSize: 18,
    border: 'none',
    borderRadius: 8,
    cursor: 'pointer',
  }
};

export default Login;
