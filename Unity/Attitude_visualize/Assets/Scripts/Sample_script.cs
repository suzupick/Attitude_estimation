using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sample_script
{
    int int_tmp;

    public Sample_script(int tmp)
    {
        this.int_tmp = tmp;
    }

    public void Hello()
    {
        Debug.Log("hello");
        Debug.Log(this.int_tmp);
    }
}
