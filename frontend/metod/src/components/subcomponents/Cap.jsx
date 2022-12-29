import { Link, useNavigate } from "react-router-dom";
import { useState } from 'react';



const Cap = () => {
    
    return (
        <>
            <div className="cap">
                <div className="colums">
                    <div class="wrap">
                        <div class="search">
                            <button type="submit" class="searchButton">
                                <i class="fa fa-search"></i>
                            </button>
                            <input type="text" class="searchTerm" placeholder="Что вас интересует?" />
                            <button type="submit" class="searchButton1">
                                    <i class="fa fa-cog"></i>
                            </button>
                        </div>
                        <div className="user">
                            <nav>
                                <ul>
                                    <li><ion-icon name="notifications-outline" style={{fontSize: "35px", color: "black", cursor: "pointer"}}></ion-icon></li>
                                    <li><ion-icon name="bookmark-outline" style={{fontSize: "35px", color: "black", cursor: "pointer"}}></ion-icon></li>
                                    <li>
                                        <div className="nav__img">
                                            <img src="https://www.meme-arsenal.com/memes/723c78e9be76eba2598c2d4c611f994c.jpg" alt="" />
                                        </div>
                                    </li>
                                </ul>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Cap;