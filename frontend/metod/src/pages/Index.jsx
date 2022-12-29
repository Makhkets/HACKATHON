import { useState } from "react";
import { Link } from "react-router-dom";
import { useEffect } from "react";


const Index = () => {

    return (
        <>
            <div className="main_index">
                <div className="stock">
                    <div className="title">
                        <p>Step to Future</p>
                    </div>
                    <div className="carousel">
                        <Link to="/information/rules">
                            <div className="card">
                                <div className="info">
                                    <p className="main">
                                        Правила ПДД!
                                    </p>
                                    <p className="desc">
                                        Карточка кликабельна
                                    </p>
                                </div>
                                <div className="img">
                                    <img src="https://i.ibb.co/6J2qddg/png-clipart-traffic-light-traffic-light-thumbnail-Photo-Room-png-Photo-Room.png" alt="" />
                                </div>
                            </div>
                        </Link>

                        <Link to="/information/advice">
                            <div className="card2">
                                <div className="info">
                                    <p className="main">
                                        Советы водителям!
                                    </p>
                                    <p className="desc">
                                        Карточка кликабельна
                                    </p>
                                </div>
                                <div className="img">
                                    <img src="https://i.ibb.co/6J2qddg/png-clipart-traffic-light-traffic-light-thumbnail-Photo-Room-png-Photo-Room.png" alt="" />
                                </div>
                            </div>
                        </Link>
                    </div>
                </div>
                
                <div className="info_block">
                    <div className="title">
                        <p>Smart TL:</p>
                    </div> 
                    <div className="desc">
                        <p>Светофор будущего - это технология , которая позволит оптимизировать трафик движения, облегчить машинам экстренных служб передвижения. 
Каким образом это будет происходить? 
Приводя в счет статистику «текст»
Однако, с нашим светофором дела будут стоять иначе. 
Это самообучеммая нейронная модель, которая каждую минуту будет анализировать дорожное движение так, чтобы на дорогах(чаще всего на перекрасках) не было скопления машин на одной стороне , в то время , когда другая сторона пустует. Модель будет выделять больше времени зеленого цвета для заполненной полосы. Также для регулировщиком и работников дпс будут отдельные анкеты , которые позволят им воздействовать на светофор для переключения цветов в ручную(при экстренных ситуациях или для пропуска кортежа)
Всем известна проблема о непосредственной задержке машин экстренных службы из-за пробок или ДТП. 
Наша модель будет в реальной времени наблюдать за происходящим на дороге и в случае включения спец сигналов , она будет переключать светофор в пользу машин экстренной службы, что позволит поскорее проехать машинам.
Перебои  с электроснабжением могут служить катализатором пробок,  чтобы справиться с этой проблемой и для увеличения функциональности этих светофоров , мы решили использовать на них солнечные батареи</p>
                    </div>
                </div>
            
            </div>
        </>
    );
};

export default Index;