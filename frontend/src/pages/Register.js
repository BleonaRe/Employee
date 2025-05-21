import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Register = () => {
  const [form, setForm] = useState({ username: '', email: '', password: '', passwordConfirm: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (form.password !== form.passwordConfirm) {
      setError("Passwords don't match");
      return;
    }
    // Këtu mund të shtosh logjikën e regjistrimit me backend

    // Për momentin ridrejtojmë tek login pas regjistrimit
    navigate('/login');
  };

  return (
    <div style={styles.container}>
      <div style={styles.box}>
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
          <input
            style={styles.input}
            type="text"
            name="username"
            placeholder="Username"
            value={form.username}
            onChange={handleChange}
            required
          />
          <input
            style={styles.input}
            type="email"
            name="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
          />
          <input
            style={styles.input}
            type="password"
            name="password"
            placeholder="Password"
            value={form.password}
            onChange={handleChange}
            required
          />
          <input
            style={styles.input}
            type="password"
            name="passwordConfirm"
            placeholder="Confirm Password"
            value={form.passwordConfirm}
            onChange={handleChange}
            required
          />
          <button style={styles.button} type="submit">Register</button>
        </form>
        {error && <p style={{ color: 'red', marginTop: 10 }}>{error}</p>}
        <p style={{ marginTop: 15 }}>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </div>
    </div>
  );
};

const styles = {
  container: {
    height: '100vh',
    background: `url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80') no-repeat center center fixed`,
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

export default Register;
