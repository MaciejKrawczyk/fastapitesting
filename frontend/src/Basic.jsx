import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";
import {BrowserRouter, Link, Route, Routes} from "react-router-dom";
import Home from "./Home.jsx";


const api = axios.create({
    baseURL: 'http://localhost:8000/'
})


function App() {
    const [count, setCount] = useState(0)
    const [students, setStudents] = useState([])

    const refreshList = async () => {
        api.get('/get-students').then(res => {
            setStudents(res.data.data)
        })
    }

    useEffect(() => {
        api.get('/get-students').then(res => {
            setStudents(res.data.data)
        })
        }, [])

    const addStudent = async () => {
        await api.post('/add-student', { first_name: "siemano", last_name: "simeano", course_id: 0, role_id: 2 })
        refreshList();
    }


  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
        </p>
      </div>
          {students.map(student => <p className="read-the-docs" key={student.id}>{student.first_name} {student.last_name}</p>)}
        <button onClick={addStudent}>kliknij aby dodac studenta</button>
        <div>
            <Link to='/'>hhhhhh</Link>
        </div>
        </div>
  )
}

export default App
