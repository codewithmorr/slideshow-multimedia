package com.example.whitelighter

import android.icu.number.Precision.increment
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.ComponentActivity
import androidx.activity.enableEdgeToEdge
import android.widget.EditText

class MainActivity : ComponentActivity() {

    private var count = 0


    private lateinit var inputNumber: EditText
    private lateinit var displayText: TextView
    private lateinit var increaseButton: Button
    private lateinit var decreaseButton: Button
    private lateinit var resetButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

       inputNumber = findViewById(R.id.inputNumber)
       displayText = findViewById(R.id.displayText)
       increaseButton = findViewById(R.id.increaseButton)
       decreaseButton = findViewById(R.id.decreaseButton)
        resetButton = findViewById(R.id.resetButton)

        increaseButton.setOnClickListener {
            val increment = inputNumber.text.toString().toIntOrNull() ?: 1
            count += increment
            displayText.text = count.toString()
        }

        decreaseButton.setOnClickListener { val decrement = inputNumber.text.toString().toIntOrNull() ?: 1
            count -= decrement
            displayText.text = count.toString()
        }

        resetButton.setOnClickListener {
            count = 0
            displayText.text = count.toString()
        }

}}
