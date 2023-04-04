import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";
import {BrowserRouter, Link, Route, Routes} from "react-router-dom";
import Home from "./Home.jsx";
import Basic from "./Basic.jsx";


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
    <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/ciul' element={<Basic />} />
    </Routes>
  )
}

export default App
