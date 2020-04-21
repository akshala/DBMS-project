import 'package:flutter/material.dart';
import 'package:football/widget/button.dart';
import 'package:football/widget/first.dart';
import 'package:football/widget/forgot.dart';
import 'package:football/widget/inputEmail.dart';
import 'package:football/widget/password.dart';
import 'package:football/widget/textLogin.dart';
import 'package:football/widget/verticalText.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
              begin: Alignment.topRight,
              end: Alignment.bottomLeft,
              colors: [Colors.blueGrey, Colors.lightBlueAccent]),
        ),
        child: ListView(
          children: <Widget>[
            Column(
              children: <Widget>[
                Row(children: <Widget>[
                  VerticalText(),
                  TextLogin(),
                ]),
                InputEmail(),
                PasswordInput(),
                ButtonLogin(),
                FirstTime(),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

// class _LoginPageState extends State<LoginPage> {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Container(
//         decoration: BoxDecoration(
//           gradient: LinearGradient(
//               begin: Alignment.topRight,
//               end: Alignment.bottomLeft,
//               colors: [Colors.blueGrey, Colors.lightBlueAccent]),
//         ),
//         child: ListView(
//           children: <Widget>[
//             Column(
//               children: <Widget>[
//                 Row(children: <Widget>[
//                   VerticalText(),
//                   TextLogin(),
//                 ]),
//                 InputEmail(),
//                 PasswordInput(),
//                 ButtonLogin(),
//                 FirstTime(),
//               ],
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }


