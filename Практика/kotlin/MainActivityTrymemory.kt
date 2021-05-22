package com.example.trytomemory

import android.content.Context
import android.content.SharedPreferences
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView

class MainActivity : AppCompatActivity()
    {
        private lateinit var prin: TextView
        var count = 0
        var mediator : SharedPreferences? = null
        override fun onCreate(savedInstanceState: Bundle?)
        {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
            mediator = getSharedPreferences("Mobile_Phone", Context.MODE_PRIVATE)
            count = mediator?.getInt("Mobile_Phone",0)!!
            prin = findViewById<TextView>(R.id.prin)
            prin.text = count.toString()
        }
        fun try_to_button(view: View)
        {
            count++
            prin.text = count.toString()
        }
        fun save(junk: Int)
        {
            mediator?.edit()?.putInt("Mobile_Phone",junk)?.apply()
        }

        override fun onDestroy() {
            super.onDestroy()
            save(count)
        }
}
