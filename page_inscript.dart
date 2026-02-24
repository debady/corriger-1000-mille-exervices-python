import 'package:flutter/material.dart';
import 'package:country_picker/country_picker.dart';

class CustomKeyboardLogin extends StatefulWidget {
  const CustomKeyboardLogin({super.key});

  @override
  State<CustomKeyboardLogin> createState() => _CustomKeyboardLoginState();
}

class _CustomKeyboardLoginState extends State<CustomKeyboardLogin> {
  String inputValue = '';
  bool isPhoneMode = true;
  final TextEditingController emailController = TextEditingController();
  String selectedCountryCode = '+225';
  Country selectedCountry = Country(
    phoneCode: '225',
    countryCode: 'CI',
    e164Sc: 0,
    geographic: true,
    level: 1,
    name: 'Côte d\'Ivoire',
    example: '0123456789',
    displayName: 'Côte d\'Ivoire (CI) [+225]',
    displayNameNoCountryCode: 'Côte d\'Ivoire (CI)',
    e164Key: '225-CI-0',
  );

  bool get isInputValid {
    if (isPhoneMode) {
      return inputValue.length == 10;
    } else {
      final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
      return emailRegex.hasMatch(emailController.text);
    }
  }

  void addDigit(String digit) {
    if (inputValue.length < 10) {
      setState(() {
        inputValue += digit;
      });
    }
  }

  void removeDigit() {
    if (inputValue.isNotEmpty) {
      setState(() {
        inputValue = inputValue.substring(0, inputValue.length - 1);
      });
    }
  }

  String formatPhoneNumber(String value) {
    if (value.isEmpty) return 'XX XX XX XX XX';
    
    final buffer = StringBuffer();
    for (int i = 0; i < value.length; i++) {
      if (i > 0 && i % 2 == 0) buffer.write(' ');
      buffer.write(value[i]);
    }
    
    String formatted = buffer.toString();
    while (formatted.length < 14) {
      if ((formatted.length + 2) <= 14) {
        formatted += ' XX';
      } else {
        formatted += 'X';
      }
    }
    
    return formatted;
  }

  Widget buildNumberKey(String number, double size) {
    return Expanded(
      child: AspectRatio(
        aspectRatio: 1,
        child: TextButton(
          onPressed: () => addDigit(number),
          style: TextButton.styleFrom(
            padding: EdgeInsets.zero,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(0),
            ),
          ),
          child: Text(
            number,
            style: TextStyle(
              fontSize: size * 0.06,
              color: Colors.black,
              fontWeight: FontWeight.w500,
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    final buttonHeight = size.width * 0.13;

    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: LayoutBuilder(
          builder: (context, constraints) {
            return SingleChildScrollView(
              child: ConstrainedBox(
                constraints: BoxConstraints(
                  minHeight: constraints.maxHeight,
                ),
                child: IntrinsicHeight(
                  child: Padding(
                    padding: EdgeInsets.all(size.width * 0.04),
                    child: Column(
                      children: [
                        SizedBox(height: size.height * 0.04),
                        Text(
                          'Bienvenue',
                          style: TextStyle(
                            fontSize: size.width * 0.06,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                        SizedBox(height: size.height * 0.01),
                        Text(
                          'chez HostoLink, pour commencer',
                          style: TextStyle(fontSize: size.width * 0.045),
                        ),
                        SizedBox(height: size.height * 0.01),
                        Text(
                          isPhoneMode
                              ? 'Veuillez taper votre Numéro de mobile'
                              : 'Veuillez taper votre Email',
                          style: TextStyle(
                            fontSize: size.width * 0.04,
                            color: Colors.green,
                          ),
                        ),
                        SizedBox(height: size.height * 0.04),
                        Container(
                          decoration: BoxDecoration(
                            border: Border(
                              bottom: BorderSide(color: Colors.grey.shade300),
                            ),
                          ),
                          child: Row(
                            children: [
                              if (isPhoneMode) ...[
                                GestureDetector(
                                  onTap: () {
                                    showCountryPicker(
                                      context: context,
                                      showPhoneCode: true,
                                      favorite: ['CI'],
                                      countryListTheme: CountryListThemeData(
                                        borderRadius: BorderRadius.circular(15),
                                        inputDecoration: InputDecoration(
                                          labelText: 'Rechercher',
                                          hintText: 'Rechercher un pays',
                                          prefixIcon: const Icon(Icons.search),
                                          border: OutlineInputBorder(
                                            borderRadius: BorderRadius.circular(15),
                                          ),
                                        ),
                                      ),
                                      onSelect: (Country country) {
                                        setState(() {
                                          selectedCountryCode = '+${country.phoneCode}';
                                          selectedCountry = country;
                                        });
                                      },
                                    );
                                  },
                                  child: Row(
                                    children: [
                                      Container(
                                        width: 30,
                                        height: 20,
                                        decoration: BoxDecoration(
                                          borderRadius: BorderRadius.circular(4),
                                        ),
                                        child: ClipRRect(
                                          borderRadius: BorderRadius.circular(4),
                                          child: Image.asset(
                                            'assets/flags/${selectedCountry.countryCode.toLowerCase()}.png',
                                            package: 'country_picker',
                                            fit: BoxFit.cover,
                                          ),
                                        ),
                                      ),
                                      const SizedBox(width: 4),
                                      Text(
                                        selectedCountryCode,
                                        style: TextStyle(fontSize: size.width * 0.04),
                                      ),
                                      const Icon(Icons.arrow_drop_down),
                                    ],
                                  ),
                                ),
                                const SizedBox(width: 8),
                                Expanded(
                                  child: Text(
                                    formatPhoneNumber(inputValue),
                                    style: TextStyle(
                                      fontSize: size.width * 0.04,
                                      color: inputValue.isEmpty ? Colors.grey : Colors.black,
                                    ),
                                  ),
                                ),
                              ] else ...[
                                Expanded(
                                  child: TextField(
                                    controller: emailController,
                                    decoration: const InputDecoration(
                                      border: InputBorder.none,
                                      hintText: 'Entrez votre email',
                                    ),
                                    keyboardType: TextInputType.emailAddress,
                                    onChanged: (value) => setState(() {}),
                                  ),
                                ),
                              ],
                              IconButton(
                                icon: Icon(
                                  isPhoneMode ? Icons.email : Icons.phone,
                                  color: Colors.red,
                                ),
                                onPressed: () {
                                  setState(() {
                                    isPhoneMode = !isPhoneMode;
                                    inputValue = '';
                                    emailController.clear();
                                  });
                                },
                              ),
                            ],
                          ),
                        ),
                        const Spacer(),
                        if (isPhoneMode) ...[
                          Container(
                            padding: EdgeInsets.symmetric(horizontal: size.width * 0.04),
                            child: Column(
                              children: [
                                Row(
                                  children: [
                                    buildNumberKey('1', size.width),
                                    buildNumberKey('2', size.width),
                                    buildNumberKey('3', size.width),
                                  ],
                                ),
                                Row(
                                  children: [
                                    buildNumberKey('4', size.width),
                                    buildNumberKey('5', size.width),
                                    buildNumberKey('6', size.width),
                                  ],
                                ),
                                Row(
                                  children: [
                                    buildNumberKey('7', size.width),
                                    buildNumberKey('8', size.width),
                                    buildNumberKey('9', size.width),
                                  ],
                                ),
                                Row(
                                  children: [
                                    Expanded(
                                      child: AspectRatio(
                                        aspectRatio: 1,
                                        child: IconButton(
                                          icon: Icon(
                                            Icons.fingerprint,
                                            size: size.width * 0.06,
                                          ),
                                          onPressed: () {},
                                        ),
                                      ),
                                    ),
                                    buildNumberKey('0', size.width),
                                    Expanded(
                                      child: AspectRatio(
                                        aspectRatio: 1,
                                        child: IconButton(
                                          icon: Icon(
                                            Icons.backspace_outlined,
                                            size: size.width * 0.06,
                                          ),
                                          onPressed: removeDigit,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                          ),
                        ],
                        SizedBox(height: size.height * 0.02),
                        SizedBox(
                          width: double.infinity,
                          height: buttonHeight,
                          child: ElevatedButton(
                            onPressed: isInputValid
                                ? () {
                                    // Navigator.push(
                                    //   context,
                                    //   MaterialPageRoute(builder: (context) => Mdp()),
                                    // );
                                  }
                                : null,
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Colors.blue,
                              disabledBackgroundColor: Colors.grey.shade300,
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(30),
                              ),
                            ),
                            child: Text(
                              'Suivant',
                              style: TextStyle(
                                fontSize: size.width * 0.045,
                                color: Colors.white,
                              ),
                            ),
                          ),
                        ),
                        SizedBox(height: size.height * 0.02),
                      ],
                    ),
                  ),
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}