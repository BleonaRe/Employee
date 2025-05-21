// src/components/Navbar.js
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Navbar = ({ username, onLogout }) => {
  return (
    <nav
      className="navbar navbar-expand-lg navbar-dark"
      style={{ background: 'linear-gradient(90deg, #500202, #4f0303)', padding: '15px' }}
    >
      <div className="container-fluid">
        <a
          className="navbar-brand"
          href="#"
          style={{ color: 'rgba(148, 33, 33, 0.853)', fontSize: '24px', fontWeight: 'bold' }}
        >
          Company
        </a>
        <div className="ms-auto dropdown">
          {username ? (
            <>
              <button
                className="btn btn-light dropdown-toggle"
                type="button"
                id="userDropdown"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                {username}
              </button>
              <ul className="dropdown-menu dropdown-menu-end" aria-labelledby="userDropdown">
                <li>
                  <a className="dropdown-item" href="/admin">
                    Admin
                  </a>
                </li>
                <li>
                  <hr className="dropdown-divider" />
                </li>
                <li>
                  <button className="dropdown-item text-danger" onClick={onLogout}>
                    Logout
                  </button>
                </li>
              </ul>
            </>
          ) : (
            <a href="/login" className="btn btn-light">
              Login
            </a>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
