/*Освоение базовых функций Android Studio */

package com.example.myapplication

import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        textView = findViewById<TextView>(R.id.textView)
        editText = findViewById<EditText>(R.id.editTextNumber)
        switch = findViewById<Switch>(R.id.switch1)
        root = findViewById<androidx.constraintlayout.widget.ConstraintLayout>(R.id.root)
        txt = findViewById<TextView>(R.id.textView2)

        switch.setOnClickListener {
            if(switch.isChecked){
                root.setBackgroundColor(Color.parseColor("#628C86"))
            }else {
                root.setBackgroundColor(Color.parseColor("#FFFFFF"))
            }
        }
    }

    private lateinit var root: androidx.constraintlayout.widget.ConstraintLayout
    private lateinit var textView: TextView
    private lateinit var editText: EditText
    private lateinit var switch: Switch

    fun countMe(view: View) {
        val countString = textView.text.toString().replace(Regex("[dp]"), "")
        var count: Int = Integer.parseInt(countString)
        var con: String
        val str = editText.text.toString()
        if (str != ""){
            var x: Int = Integer.parseInt(str)
            count += x
        } else{
            count ++
        }
        con=count.toString() + "dp"
        if ((count - 1) % 10 == 9)
        {
            val temp = Toast.makeText(this, con, Toast.LENGTH_SHORT)
            temp.show()
        }
        textView.text=con.toString()
    }
    private lateinit var txt: TextView
    fun but1(view: View){
        val x = "Name, Age \n Раб"
        txt.text=x.toString()
    }
    fun but2(view: View){
        val x = "Name, Age \n Безработный"
        txt.text=x.toString()
    }
}
