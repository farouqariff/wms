import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function ManagerPage() {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user") || "{}");

  useEffect(() => {
    fetchPageData();
  }, []);

  const fetchPageData = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/pages/manager/", {
        credentials: "include",
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message);
      } else {
        setError(data.error || "Access denied");
      }
    } catch (err) {
      setError("Connection error");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    try {
      await fetch("http://localhost:8000/api/logout/", {
        method: "POST",
        credentials: "include",
      });
      localStorage.removeItem("user");
      navigate("/");
    } catch (err) {
      console.error("Logout error:", err);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center">
        <div className="text-white text-xl">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center p-4">
        <div className="bg-slate-800 rounded-xl shadow-2xl p-8 border border-slate-700 max-w-md w-full text-center">
          <div className="text-red-400 text-6xl mb-4">⛔</div>
          <h2 className="text-2xl font-bold text-white mb-4">Access Denied</h2>
          <p className="text-slate-400 mb-6">{error}</p>
          <button
            onClick={() => navigate("/")}
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-lg transition"
          >
            Go to Login
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4">
      <div className="max-w-4xl mx-auto py-8">
        {/* Header */}
        <div className="bg-slate-800 rounded-xl shadow-2xl p-6 border border-slate-700 mb-6">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-3xl font-bold text-white mb-2">
                Manager Dashboard
              </h1>
              <p className="text-slate-400">Welcome, {user.username}</p>
            </div>
            <button
              onClick={handleLogout}
              className="bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-lg transition"
            >
              Logout
            </button>
          </div>
        </div>

        {/* Main Content */}
        <div className="bg-slate-800 rounded-xl shadow-2xl p-8 border border-slate-700 text-center">
          <div className="text-purple-400 text-6xl mb-4">👔</div>
          <h2 className="text-3xl font-bold text-white mb-4">{message}</h2>
          <p className="text-slate-400 mb-6">
            You have manager-level access to the system.
          </p>

          <div className="bg-slate-700 rounded-lg p-4 mt-6">
            <p className="text-slate-300 text-sm">
              Role:{" "}
              <span className="text-purple-400 font-semibold">Manager</span>
            </p>
            <p className="text-slate-300 text-sm mt-2">
              Permissions: View Manager Page
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ManagerPage;
