import 'package:flutter/material.dart';



class PageEnvoiArgent extends StatefulWidget {
  const PageEnvoiArgent({super.key});

  @override
  State<PageEnvoiArgent> createState() => _PageEnvoiArgentState();
}

class _PageEnvoiArgentState extends State<PageEnvoiArgent> {
final _amountController = TextEditingController();
 double montantRecu = 0;
 
 void _calculateMontantRecu() {
   if (_amountController.text.isNotEmpty) {
     double montant = double.parse(_amountController.text);
     setState(() {
       montantRecu = montant - (montant * 0); // Frais 0.5%
      //  montantRecu = montant - (montant * 0.005); // Frais 0.5%
     });
   }
 }

 @override
 Widget build(BuildContext context) {
   return Scaffold(
     backgroundColor: Colors.white,
     body: SafeArea(
       child: Padding(
         padding: const EdgeInsets.all(20),
         child: Column(
           children: [
             const Text(
               'Envoyer de l\'argent à',
               style: TextStyle(
                 fontSize: 24,
                 fontWeight: FontWeight.w500
               ),
               textAlign: TextAlign.center,
             ),
             const SizedBox(height: 30),
             
             Image.network(
               'https://res.cloudinary.com/dhrrk7vsd/image/upload/v1740668911/hostolink/uxjfpnsjxgcadsun2i86.png',
               width: 80,
               height: 80,
             ),
             
             const SizedBox(height: 40),
             
             Row(
               children: [
                 CircleAvatar(
                   backgroundColor: Colors.blue[100],
                   child: Icon(Icons.person, color: Colors.blue),
                 ),
                 const SizedBox(width: 15),
                 Column(
                   crossAxisAlignment: CrossAxisAlignment.start,
                   children: [
                     Text('Alice', 
                       style: TextStyle(fontSize: 18)
                     ),
                     Text('+225074841270',
                       style: TextStyle(
                         color: Colors.grey[600],
                         fontSize: 16
                       )
                     ),
                   ],
                 )
               ],
             ),
             
             const SizedBox(height: 40),
             
             Column(
               crossAxisAlignment: CrossAxisAlignment.start,
               children: [
                 Text('Montant Envoyé',
                   style: TextStyle(
                     color: Colors.grey[600],
                     fontSize: 16
                   )
                 ),
                 TextField(
                   controller: _amountController,
                   keyboardType: TextInputType.number,
                   onChanged: (value) => _calculateMontantRecu(),
                   decoration: InputDecoration(
                     border: UnderlineInputBorder(),
                   ),
                 ),
                 
                 Padding(
                   padding: EdgeInsets.symmetric(vertical: 10),
                   child: Row(
                     mainAxisAlignment: MainAxisAlignment.spaceBetween,
                     children: [
                       Text('100 000 F FCFA'),
                       Text('Frais 0.5%', 
                         style: TextStyle(color: Colors.green)
                       ),
                       Text('500 F CFA'),
                     ],
                   ),
                 ),
               ],
             ),
             
             const SizedBox(height: 30),
             
             Text('Montant Reçu',
               style: TextStyle(fontSize: 18)
             ),
             Text(
               '${montantRecu.toStringAsFixed(0)} F CFA',
               style: TextStyle(fontSize: 16, color: Colors.grey),
             ),
             
             Spacer(),
             
             SizedBox(
               width: double.infinity,
               height: 50,
               child: ElevatedButton(
                 onPressed: () {
                   Navigator.push(
                     context,
                     MaterialPageRoute(builder: (context) => ConfirmationPage())
                   );
                 },
                 // ignore: sort_child_properties_last
                 child: Text('Envoyer'),
                 style: ElevatedButton.styleFrom(
                   backgroundColor: Colors.grey[300],
                   foregroundColor: Colors.black,
                   shape: RoundedRectangleBorder(
                     borderRadius: BorderRadius.circular(25)
                   ),
                 ),
               ),
             ),
           ],
         ),
       ),
     ),
   );
 }
}

// ignore: use_key_in_widget_constructors
class ConfirmationPage extends StatelessWidget {
 @override 
 Widget build(BuildContext context) {
   return Scaffold(
     appBar: AppBar(
       title: Text('Confirmation'),
     ),
     body: Center(
       child: Text('Transfert confirmé'),
     ),
   );
 }


}