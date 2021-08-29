import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Header from "./Header/Header";
import Login from "./Login/Login";
import Register from "./Register/Register";
import StartTrade from "./StartTrade/StartTrade";
import MyTradesBorrower from "./MyTradesBorrower/MyTradesBorrower";


function App() {
    return (
        <Router>
            <Header />
            <Switch>
                <Route path='/login' exact component={Login} />
                <Route path='/register' exact component={Register} />
                <Route path='/start-trade' exact component={StartTrade} />
                <Route path='/my-trades-borrower' exact component={MyTradesBorrower} />
            </Switch>
        </Router>
    );

}

export default App;
