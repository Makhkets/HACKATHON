import { useState } from "react";
import { Link } from "react-router-dom";
import { useEffect } from "react";


const Index = () => {

    const [patients, setPatients] = useState(false)

    
    useEffect(() => {
        // (async () => {
        //     const data = await getPatients()
        //     setPatients(data)
        // })()
    }, []);
    

    return (
        <>
            <h1>из Index.jsx</h1>
        </>
    );
};

export default Index;