 
import 'package:flutter/material.dart';
import 'package:football/player_menu.dart';
import 'package:football/manager_menu.dart';
import 'package:football/club_menu.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
        // This makes the visual density adapt to the platform that you run
        // the app on. For desktop platforms, the controls will be smaller and
        // closer together (more dense) than on mobile platforms.
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  // MyHomePage({Key key, this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Color.fromRGBO(42, 54, 63, 1),
      child: Center(
        child: Container(
        // mainAxisAlignment: MainAxisAlignment.center,
        margin: const EdgeInsets.all(10.0),
        width: 450.0,
        height: 600.0,
        decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topRight,
              end: Alignment.bottomLeft,
              colors: [Colors.cyan[900], Colors.cyan[50]]),
          shape: BoxShape.rectangle,
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(75.0),
            bottomRight: Radius.circular(75.0)
          ) 
        ),
        child: Material(
          type:MaterialType.transparency,
          child:Column(

            children: <Widget>[Login()],
          )
        )
      ))
    );
  }
}

class Login extends StatefulWidget {
  // name({Key key}) : super(key: key);

  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login> {
  TextEditingController user = new TextEditingController();
  TextEditingController pass = new TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: new EdgeInsets.all(50.0),
      // padding: new EdgeInsets.only(top:100.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children:[
          TextField(
            controller: user,
            cursorColor: Colors.red,
            obscureText: false,
            style: new TextStyle(
              color: Colors.white,                
              fontFamily: 'Montserrat',
              fontWeight: FontWeight.w600,), 
            decoration: InputDecoration(
              enabledBorder: OutlineInputBorder(
//               style: Theme.of(context).textTheme.headline4,
//             ),
//           ],
//         ),
//       ),
//       floatingActionButton: FloatingActionButton(
                // borderWeight: Border
                borderRadius: BorderRadius.circular(15),
                borderSide: BorderSide(width:2.0, color:Colors.white),
              ),
              // contentPadding: EdgeInsets.all(200.0),
              labelText: 'Username',
              labelStyle: TextStyle(
                fontFamily: 'Montserrat',
                fontWeight: FontWeight.w600,
                color: Colors.white
              ),
            ),
          ),
          SizedBox(height: 30),
          TextField(
            controller: pass,
            cursorColor: Colors.red,
            obscureText: true,
            style: new TextStyle(
              color: Colors.white,                
              fontFamily: 'Montserrat',
              fontWeight: FontWeight.w600,),  
            decoration: InputDecoration(
              enabledBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(15),
                borderSide: BorderSide(width:2.0, color:Colors.white),
                // borderSide: BorderSide(color:),
              ),
              labelText: 'Password',
              labelStyle: TextStyle(
                fontFamily: 'Montserrat',
                fontWeight: FontWeight.w600,
                color: Colors.white
              ),
            ),
          ),
          SizedBox(height: 30),
          Container(
            height: 50.0,
            child: RaisedButton(
              onPressed: (){
                // navigate to player page
                if(user.text == 'player'){
                    Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => player_page()),
                  );
                }
                if(user.text == 'manager'){
                    Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => manager_page()),
                  );
                }
                if(user.text == 'club'){
                    Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => club_page()),
                  );
                }
              },
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(80.0)),
              padding: EdgeInsets.all(0.0),
              child: Ink(
                decoration: BoxDecoration(
                    gradient: LinearGradient(colors: [Color(0xff374ABE), Color(0xff64B6FF)],
                      begin: Alignment.centerLeft,
                      end: Alignment.centerRight,
                    ),
                    borderRadius: BorderRadius.circular(30.0),
                    // borderSide: BorderSide(width:2.0, color:Colors.white),
                ),
                child: Container(
                  constraints: BoxConstraints(maxWidth: 300.0, minHeight: 50.0),
                  alignment: Alignment.center,
                  child: Text(
                    "Login",
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontFamily: 'Montserrat',
                      fontWeight: FontWeight.w900,
                      color: Colors.white
                    ),
                  ),
                ),
              ),
            ),
          ),
        ]  
      ),
    );
  }
}

// class _MyHomePageState extends State<MyHomePage> {
//   int _counter = 0;

//   void _incrementCounter() {
//     setState(() {
//       // This call to setState tells the Flutter framework that something has
//       // changed in this State, which causes it to rerun the build method below
//       // so that the display can reflect the updated values. If we changed
//       // _counter without calling setState(), then the build method would not be
//       // called again, and so nothing would appear to happen.
//       _counter++;
//     });
//   }

//   @override
//   Widget build(BuildContext context) {
//     // This method is rerun every time setState is called, for instance as done
//     // by the _incrementCounter method above.
//     //
//     // The Flutter framework has been optimized to make rerunning build methods
//     // fast, so that you can just rebuild anything that needs updating rather
//     // than having to individually change instances of widgets.
//     return Scaffold(
//       appBar: AppBar(
//         // Here we take the value from the MyHomePage object that was created by
//         // the App.build method, and use it to set our appbar title.
//         title: Text(widget.title),
//       ),
//       body: Center(
//         // Center is a layout widget. It takes a single child and positions it
//         // in the middle of the parent.
//         child: Column(
//           // Column is also a layout widget. It takes a list of children and
//           // arranges them vertically. By default, it sizes itself to fit its
//           // children horizontally, and tries to be as tall as its parent.
//           //
//           // Invoke "debug painting" (press "p" in the console, choose the
//           // "Toggle Debug Paint" action from the Flutter Inspector in Android
//           // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
//           // to see the wireframe for each widget.
//           //
//           // Column has various properties to control how it sizes itself and
//           // how it positions its children. Here we use mainAxisAlignment to
//           // center the children vertically; the main axis here is the vertical
//           // axis because Columns are vertical (the cross axis would be
//           // horizontal).
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: <Widget>[
//             Text(
//               'You have pushed the button this many times:',
//             ),
//             Text(
//               '$_counter',
//               style: Theme.of(context).textTheme.headline4,
//             ),
//           ],
//         ),
//       ),
//       floatingActionButton: FloatingActionButton(
//         onPressed: _incrementCounter,
//         tooltip: 'Increment',
//         child: Icon(Icons.add),
//       ), // This trailing comma makes auto-formatting nicer for build methods.
//     );
//   }
// }