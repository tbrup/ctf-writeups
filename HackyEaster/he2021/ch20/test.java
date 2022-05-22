/*
 * Decompiled with CFR 0.151.
 * 
 * Could not load the following classes:
 *  groovy.lang.Binding
 *  groovy.lang.GroovyObject
 *  groovy.lang.MetaClass
 *  groovy.lang.Script
 *  org.codehaus.groovy.reflection.ClassInfo
 *  org.codehaus.groovy.runtime.GStringImpl
 *  org.codehaus.groovy.runtime.InvokerHelper
 *  org.codehaus.groovy.runtime.ScriptBytecodeAdapter
 *  org.codehaus.groovy.runtime.callsite.CallSite
 *  org.codehaus.groovy.runtime.callsite.CallSiteArray
 *  org.codehaus.groovy.runtime.typehandling.DefaultTypeTransformation
 */
import groovy.lang.Binding;
import groovy.lang.GroovyObject;
import groovy.lang.MetaClass;
import groovy.lang.Script;
import java.lang.ref.SoftReference;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import org.codehaus.groovy.reflection.ClassInfo;
import org.codehaus.groovy.runtime.GStringImpl;
import org.codehaus.groovy.runtime.InvokerHelper;
import org.codehaus.groovy.runtime.ScriptBytecodeAdapter;
import org.codehaus.groovy.runtime.callsite.CallSite;
import org.codehaus.groovy.runtime.callsite.CallSiteArray;
import org.codehaus.groovy.runtime.typehandling.DefaultTypeTransformation;

public class runme
extends Script {
    private static /* synthetic */ ClassInfo $staticClassInfo;
    public static transient /* synthetic */ boolean __$stMC;
    private static /* synthetic */ SoftReference $callSiteArray;

    public runme() {
        CallSite[] callSiteArray = runme.$getCallSiteArray();
    }

    public runme(Binding context) {
        CallSite[] callSiteArray = runme.$getCallSiteArray();
        super(context);
    }

    public static void main(String ... args) {
        CallSite[] callSiteArray = runme.$getCallSiteArray();
        callSiteArray[0].call(InvokerHelper.class, runme.class, (Object)args);
    }

    public Object run() {
        CallSite[] callSiteArray = runme.$getCallSiteArray();
        Set a = (Set)ScriptBytecodeAdapter.asType((Object)ScriptBytecodeAdapter.createList((Object[])new Object[]{7, 3, 2}), Set.class);
        List b = ScriptBytecodeAdapter.createList((Object[])new Object[]{7, 8, a, 4, 5, 3, 5, 1, ScriptBytecodeAdapter.createList((Object[])new Object[]{3, 0}), 3, 4, 5, 5});
        Object s = callSiteArray[1].call((Object)ScriptBytecodeAdapter.createList((Object[])new Object[]{1, 6, a, 9, 4, ScriptBytecodeAdapter.createList((Object[])new Object[]{5, 3, 4}), 8, 9, 1, a, 3, 3}), (Object)b);
        String cipher = "ik934:\u007fnvr|h2>biu37~\u0080bdeg|D~";
        String sol = "";
        Object i = null;
        Iterator iterator = (Iterator)ScriptBytecodeAdapter.castToType((Object)callSiteArray[2].call((Object)ScriptBytecodeAdapter.createRange((Object)0, (Object)27, (boolean)true)), Iterator.class);
        while (iterator.hasNext()) {
            i = iterator.next();
            callSiteArray[3].call((Object)sol, (Object)Character.valueOf(DefaultTypeTransformation.charUnbox((Object)callSiteArray[4].call(callSiteArray[5].call((Object)cipher, i), callSiteArray[6].call(callSiteArray[7].call(s), i)))));
        }
        return callSiteArray[8].callCurrent((GroovyObject)this, (Object)new GStringImpl(new Object[]{sol}, new String[]{"The flag is: ", ""}));
    }

    protected /* synthetic */ MetaClass $getStaticMetaClass() {
        if (((Object)((Object)this)).getClass() != runme.class) {
            return ScriptBytecodeAdapter.initMetaClass((Object)((Object)this));
        }
        ClassInfo classInfo = $staticClassInfo;
        if (classInfo == null) {
            $staticClassInfo = classInfo = ClassInfo.getClassInfo(((Object)((Object)this)).getClass());
        }
        return classInfo.getMetaClass();
    }

    private static /* synthetic */ void $createCallSiteArray_1(String[] stringArray) {
        stringArray[0] = "runScript";
        stringArray[1] = "plus";
        stringArray[2] = "iterator";
        stringArray[3] = "plus";
        stringArray[4] = "minus";
        stringArray[5] = "charAt";
        stringArray[6] = "getAt";
        stringArray[7] = "flatten";
        stringArray[8] = "println";
    }

    private static /* synthetic */ CallSiteArray $createCallSiteArray() {
        String[] stringArray = new String[9];
        runme.$createCallSiteArray_1(stringArray);
        return new CallSiteArray(runme.class, stringArray);
    }

    private static /* synthetic */ CallSite[] $getCallSiteArray() {
        CallSiteArray callSiteArray;
        if ($callSiteArray == null || (callSiteArray = (CallSiteArray)$callSiteArray.get()) == null) {
            callSiteArray = runme.$createCallSiteArray();
            $callSiteArray = new SoftReference<CallSiteArray>(callSiteArray);
        }
        return callSiteArray.array;
    }
}
