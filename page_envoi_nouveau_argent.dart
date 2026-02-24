import 'package:flutter/material.dart';

class PageEnvoiNouveauArgent extends StatefulWidget {
  const PageEnvoiNouveauArgent({super.key});

  @override
  State<PageEnvoiNouveauArgent> createState() => _PageEnvoiNouveauArgentState();
}

class _PageEnvoiNouveauArgentState extends State<PageEnvoiNouveauArgent> {
  final _phoneController = TextEditingController();
  final _amountController = TextEditingController();
  double montantRecu = 0;

  void _calculateMontantRecu() {
    if (_amountController.text.isNotEmpty) {
      double montant = double.parse(_amountController.text);
      setState(() {
        montantRecu = montant - (montant * 0);
        // montantRecu = montant - (montant * 0.005);
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
                    fontWeight: FontWeight.w500,
                    fontFamily: 'Serif'),
              ),
              const SizedBox(height: 30),
              Image.network(
                'https://res.cloudinary.com/dhrrk7vsd/image/upload/v1740668911/hostolink/uxjfpnsjxgcadsun2i86.png',
                width: 80,
                height: 80,
              ),
              const SizedBox(height: 40),
              TextField(
                controller: _phoneController,
                keyboardType: TextInputType.phone,
                decoration: InputDecoration(
                  hintText: 'Saisissez le numéro ici..',
                  hintStyle: TextStyle(color: Colors.grey[400]),
                  border: UnderlineInputBorder(),
                ),
              ),
              const SizedBox(height: 40),
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
                    Text('100 000 F FCFA',
                        style: TextStyle(color: Colors.grey[600])),
                    Text('Frais 0.5%', style: TextStyle(color: Colors.green)),
                    Text('500 F CFA',
                        style: TextStyle(color: Colors.grey[600])),
                  ],
                ),
              ),
              const SizedBox(height: 20),
              Text('Montant Reçu',
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500)),
              Text(
                '${montantRecu.toStringAsFixed(0)} F CFA',
                style: TextStyle(fontSize: 16, color: Colors.grey),
              ),
              Spacer(),
              SizedBox(
                width: double.infinity,
                height: 50,
                // child: ElevatedButton(
                //   onPressed: () {
                //     Navigator.push(context,
                //         // MaterialPageRoute(builder: (context) => TransferPage(transactionData: null,))
                //         //  MaterialPageRoute(builder: (context) => ConfirmationPage())
                //         );
                //   },
                //   child: Text('Envoyer', style: TextStyle(fontSize: 18)),
                //   style: ElevatedButton.styleFrom(
                //     backgroundColor: Colors.grey[300],
                //     foregroundColor: Colors.black,
                //     shape: RoundedRectangleBorder(
                //         borderRadius: BorderRadius.circular(25)),
                //   ),
                // ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// class ConfirmationPage extends StatelessWidget {
//  @override 
//  Widget build(BuildContext context) {
//    return Scaffold(
//      appBar: AppBar(
//        title: Text('Confirmation'),
//      ),
//      body: Center(
//        child: Text('Transfert confirmé'),
//      ),
//    );
//  }


// }
