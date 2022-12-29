import { useState } from "react";
import { Link } from "react-router-dom";
import { useEffect } from "react";


const TrafficLight = () => {
    const [color, setColor] = useState(0)

    function delay(time) {
        return new Promise(resolve => setTimeout(resolve, time));
      }

    function RQ() {
        function T() {
            setTimeout(() => { setColor("red"); }, 3000);
            setTimeout(() => { setColor("yellow"); }, 6000); 
            setTimeout(() => { setColor("green"); }, 9000); 
        }

        setTimeout(() => { T() }, 3000);
        setTimeout(() => { T() }, 18000);
        setTimeout(() => { T() }, 27000);
        
    }

    return (
        <>
            <div className="light_information">
                <div className="cap">
                    <p>БЕТА ВЕРСИЯ СВЕТОФОРА</p>
                </div>
                <div className="container">
                    <div className="traffic">
                        <div className="block">
                            <div className="_1" style={{backgroundColor: color === "red" ? "red" : "gray"}}></div>
                            <div className="_2" style={{backgroundColor: color === "yellow" ? "yellow" : "gray"}}></div>
                            <div className="_3" style={{backgroundColor: color === "green" ? "green" : "gray"}}></div>
                        </div>
                    </div>
                    <div className="info">
                        <div className="title">
                            <p>Как работает наш светофор?</p>
                        </div>
                        <div className="desc">
                            <p>
                            Это самообучеммая нейронная модель, которая каждую минуту будет анализировать дорожное движение так, чтобы на дорогах(чаще всего на перекрасках) не было скопления машин на одной стороне , в то время , когда другая сторона пустует. Модель будет выделять больше времени зеленого цвета для заполненной полосы.
                            </p>
                            <button className="traffifc_button" onClick={RQ}>Запросить состояние</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default TrafficLight;