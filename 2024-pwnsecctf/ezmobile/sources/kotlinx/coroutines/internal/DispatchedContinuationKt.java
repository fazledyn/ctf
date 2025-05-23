package kotlinx.coroutines.internal;

import kotlin.Metadata;
import kotlin.Unit;
import kotlin.coroutines.Continuation;
import kotlin.jvm.functions.Function0;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.InlineMarker;
import kotlinx.coroutines.DebugKt;
import kotlinx.coroutines.DispatchedTask;
import kotlinx.coroutines.EventLoop;
import kotlinx.coroutines.ThreadLocalEventLoop;

@Metadata(d1 = {"\u0000J\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\u001a;\u0010\u0006\u001a\u00020\u0007*\u0006\u0012\u0002\b\u00030\b2\b\u0010\t\u001a\u0004\u0018\u00010\n2\u0006\u0010\u000b\u001a\u00020\f2\b\b\u0002\u0010\r\u001a\u00020\u00072\f\u0010\u000e\u001a\b\u0012\u0004\u0012\u00020\u00100\u000fH\b\u001aU\u0010\u0011\u001a\u00020\u0010\"\u0004\b\u0000\u0010\u0012*\b\u0012\u0004\u0012\u0002H\u00120\u00132\f\u0010\u0014\u001a\b\u0012\u0004\u0012\u0002H\u00120\u00152%\b\u0002\u0010\u0016\u001a\u001f\u0012\u0013\u0012\u00110\u0018¢\u0006\f\b\u0019\u0012\b\b\u001a\u0012\u0004\b\b(\u001b\u0012\u0004\u0012\u00020\u0010\u0018\u00010\u0017H\u0007ø\u0001\u0000¢\u0006\u0002\u0010\u001c\u001a\u0012\u0010\u001d\u001a\u00020\u0007*\b\u0012\u0004\u0012\u00020\u00100\bH\u0000\"\u0016\u0010\u0000\u001a\u00020\u00018\u0000X\u0004¢\u0006\b\n\u0000\u0012\u0004\b\u0002\u0010\u0003\"\u0016\u0010\u0004\u001a\u00020\u00018\u0002X\u0004¢\u0006\b\n\u0000\u0012\u0004\b\u0005\u0010\u0003\u0002\u0004\n\u0002\b\u0019¨\u0006\u001e"}, d2 = {"REUSABLE_CLAIMED", "Lkotlinx/coroutines/internal/Symbol;", "getREUSABLE_CLAIMED$annotations", "()V", "UNDEFINED", "getUNDEFINED$annotations", "executeUnconfined", "", "Lkotlinx/coroutines/internal/DispatchedContinuation;", "contState", "", "mode", "", "doYield", "block", "Lkotlin/Function0;", "", "resumeCancellableWith", "T", "Lkotlin/coroutines/Continuation;", "result", "Lkotlin/Result;", "onCancellation", "Lkotlin/Function1;", "", "Lkotlin/ParameterName;", "name", "cause", "(Lkotlin/coroutines/Continuation;Ljava/lang/Object;Lkotlin/jvm/functions/Function1;)V", "yieldUndispatched", "kotlinx-coroutines-core"}, k = 2, mv = {1, 6, 0}, xi = 48)
/* compiled from: DispatchedContinuation.kt */
public final class DispatchedContinuationKt {
    public static final Symbol REUSABLE_CLAIMED = new Symbol("REUSABLE_CLAIMED");
    /* access modifiers changed from: private */
    public static final Symbol UNDEFINED = new Symbol("UNDEFINED");

    public static /* synthetic */ void getREUSABLE_CLAIMED$annotations() {
    }

    private static /* synthetic */ void getUNDEFINED$annotations() {
    }

    public static /* synthetic */ void resumeCancellableWith$default(Continuation continuation, Object obj, Function1 function1, int i, Object obj2) {
        if ((i & 2) != 0) {
            function1 = null;
        }
        resumeCancellableWith(continuation, obj, function1);
    }

    /* JADX WARNING: Code restructure failed: missing block: B:25:0x00a1, code lost:
        if (r9.clearThreadContext() != false) goto L_0x00a3;
     */
    /* Code decompiled incorrectly, please refer to instructions dump. */
    public static final <T> void resumeCancellableWith(kotlin.coroutines.Continuation<? super T> r7, java.lang.Object r8, kotlin.jvm.functions.Function1<? super java.lang.Throwable, kotlin.Unit> r9) {
        /*
            boolean r0 = r7 instanceof kotlinx.coroutines.internal.DispatchedContinuation
            if (r0 == 0) goto L_0x00c7
            kotlinx.coroutines.internal.DispatchedContinuation r7 = (kotlinx.coroutines.internal.DispatchedContinuation) r7
            java.lang.Object r9 = kotlinx.coroutines.CompletionStateKt.toState((java.lang.Object) r8, (kotlin.jvm.functions.Function1<? super java.lang.Throwable, kotlin.Unit>) r9)
            kotlinx.coroutines.CoroutineDispatcher r0 = r7.dispatcher
            kotlin.coroutines.CoroutineContext r1 = r7.getContext()
            boolean r0 = r0.isDispatchNeeded(r1)
            r1 = 1
            if (r0 == 0) goto L_0x0028
            r7._state = r9
            r7.resumeMode = r1
            kotlinx.coroutines.CoroutineDispatcher r8 = r7.dispatcher
            kotlin.coroutines.CoroutineContext r9 = r7.getContext()
            java.lang.Runnable r7 = (java.lang.Runnable) r7
            r8.dispatch(r9, r7)
            goto L_0x00ca
        L_0x0028:
            kotlinx.coroutines.DebugKt.getASSERTIONS_ENABLED()
            kotlinx.coroutines.ThreadLocalEventLoop r0 = kotlinx.coroutines.ThreadLocalEventLoop.INSTANCE
            kotlinx.coroutines.EventLoop r0 = r0.getEventLoop$kotlinx_coroutines_core()
            boolean r2 = r0.isUnconfinedLoopActive()
            if (r2 == 0) goto L_0x0042
            r7._state = r9
            r7.resumeMode = r1
            kotlinx.coroutines.DispatchedTask r7 = (kotlinx.coroutines.DispatchedTask) r7
            r0.dispatchUnconfined(r7)
            goto L_0x00ca
        L_0x0042:
            r2 = r7
            kotlinx.coroutines.DispatchedTask r2 = (kotlinx.coroutines.DispatchedTask) r2
            r0.incrementUseCount(r1)
            r3 = 0
            kotlin.coroutines.CoroutineContext r4 = r7.getContext()     // Catch:{ all -> 0x00ba }
            kotlinx.coroutines.Job$Key r5 = kotlinx.coroutines.Job.Key     // Catch:{ all -> 0x00ba }
            kotlin.coroutines.CoroutineContext$Key r5 = (kotlin.coroutines.CoroutineContext.Key) r5     // Catch:{ all -> 0x00ba }
            kotlin.coroutines.CoroutineContext$Element r4 = r4.get(r5)     // Catch:{ all -> 0x00ba }
            kotlinx.coroutines.Job r4 = (kotlinx.coroutines.Job) r4     // Catch:{ all -> 0x00ba }
            if (r4 == 0) goto L_0x007b
            boolean r5 = r4.isActive()     // Catch:{ all -> 0x00ba }
            if (r5 != 0) goto L_0x007b
            java.util.concurrent.CancellationException r8 = r4.getCancellationException()     // Catch:{ all -> 0x00ba }
            r4 = r8
            java.lang.Throwable r4 = (java.lang.Throwable) r4     // Catch:{ all -> 0x00ba }
            r7.cancelCompletedResult$kotlinx_coroutines_core(r9, r4)     // Catch:{ all -> 0x00ba }
            kotlin.coroutines.Continuation r7 = (kotlin.coroutines.Continuation) r7     // Catch:{ all -> 0x00ba }
            kotlin.Result$Companion r9 = kotlin.Result.Companion     // Catch:{ all -> 0x00ba }
            java.lang.Throwable r8 = (java.lang.Throwable) r8     // Catch:{ all -> 0x00ba }
            java.lang.Object r8 = kotlin.ResultKt.createFailure(r8)     // Catch:{ all -> 0x00ba }
            java.lang.Object r8 = kotlin.Result.m155constructorimpl(r8)     // Catch:{ all -> 0x00ba }
            r7.resumeWith(r8)     // Catch:{ all -> 0x00ba }
            goto L_0x00a6
        L_0x007b:
            kotlin.coroutines.Continuation<T> r9 = r7.continuation     // Catch:{ all -> 0x00ba }
            java.lang.Object r4 = r7.countOrElement     // Catch:{ all -> 0x00ba }
            kotlin.coroutines.CoroutineContext r5 = r9.getContext()     // Catch:{ all -> 0x00ba }
            java.lang.Object r4 = kotlinx.coroutines.internal.ThreadContextKt.updateThreadContext(r5, r4)     // Catch:{ all -> 0x00ba }
            kotlinx.coroutines.internal.Symbol r6 = kotlinx.coroutines.internal.ThreadContextKt.NO_THREAD_ELEMENTS     // Catch:{ all -> 0x00ba }
            if (r4 == r6) goto L_0x0090
            kotlinx.coroutines.UndispatchedCoroutine r9 = kotlinx.coroutines.CoroutineContextKt.updateUndispatchedCompletion(r9, r5, r4)     // Catch:{ all -> 0x00ba }
            goto L_0x0094
        L_0x0090:
            r9 = r3
            kotlinx.coroutines.UndispatchedCoroutine r9 = (kotlinx.coroutines.UndispatchedCoroutine) r9     // Catch:{ all -> 0x00ba }
            r9 = r3
        L_0x0094:
            kotlin.coroutines.Continuation<T> r7 = r7.continuation     // Catch:{ all -> 0x00ad }
            r7.resumeWith(r8)     // Catch:{ all -> 0x00ad }
            kotlin.Unit r7 = kotlin.Unit.INSTANCE     // Catch:{ all -> 0x00ad }
            if (r9 == 0) goto L_0x00a3
            boolean r7 = r9.clearThreadContext()     // Catch:{ all -> 0x00ba }
            if (r7 == 0) goto L_0x00a6
        L_0x00a3:
            kotlinx.coroutines.internal.ThreadContextKt.restoreThreadContext(r5, r4)     // Catch:{ all -> 0x00ba }
        L_0x00a6:
            boolean r7 = r0.processUnconfinedEvent()     // Catch:{ all -> 0x00ba }
            if (r7 != 0) goto L_0x00a6
            goto L_0x00be
        L_0x00ad:
            r7 = move-exception
            if (r9 == 0) goto L_0x00b6
            boolean r8 = r9.clearThreadContext()     // Catch:{ all -> 0x00ba }
            if (r8 == 0) goto L_0x00b9
        L_0x00b6:
            kotlinx.coroutines.internal.ThreadContextKt.restoreThreadContext(r5, r4)     // Catch:{ all -> 0x00ba }
        L_0x00b9:
            throw r7     // Catch:{ all -> 0x00ba }
        L_0x00ba:
            r7 = move-exception
            r2.handleFatalException(r7, r3)     // Catch:{ all -> 0x00c2 }
        L_0x00be:
            r0.decrementUseCount(r1)
            goto L_0x00ca
        L_0x00c2:
            r7 = move-exception
            r0.decrementUseCount(r1)
            throw r7
        L_0x00c7:
            r7.resumeWith(r8)
        L_0x00ca:
            return
        */
        throw new UnsupportedOperationException("Method not decompiled: kotlinx.coroutines.internal.DispatchedContinuationKt.resumeCancellableWith(kotlin.coroutines.Continuation, java.lang.Object, kotlin.jvm.functions.Function1):void");
    }

    public static final boolean yieldUndispatched(DispatchedContinuation<? super Unit> dispatchedContinuation) {
        Unit unit = Unit.INSTANCE;
        DebugKt.getASSERTIONS_ENABLED();
        EventLoop eventLoop$kotlinx_coroutines_core = ThreadLocalEventLoop.INSTANCE.getEventLoop$kotlinx_coroutines_core();
        if (eventLoop$kotlinx_coroutines_core.isUnconfinedQueueEmpty()) {
            return false;
        }
        if (eventLoop$kotlinx_coroutines_core.isUnconfinedLoopActive()) {
            dispatchedContinuation._state = unit;
            dispatchedContinuation.resumeMode = 1;
            eventLoop$kotlinx_coroutines_core.dispatchUnconfined(dispatchedContinuation);
            return true;
        }
        DispatchedTask dispatchedTask = dispatchedContinuation;
        eventLoop$kotlinx_coroutines_core.incrementUseCount(true);
        try {
            dispatchedContinuation.run();
            do {
            } while (eventLoop$kotlinx_coroutines_core.processUnconfinedEvent());
        } catch (Throwable th) {
            eventLoop$kotlinx_coroutines_core.decrementUseCount(true);
            throw th;
        }
        eventLoop$kotlinx_coroutines_core.decrementUseCount(true);
        return false;
    }

    private static final boolean executeUnconfined(DispatchedContinuation<?> dispatchedContinuation, Object obj, int i, boolean z, Function0<Unit> function0) {
        if (!DebugKt.getASSERTIONS_ENABLED() || i != -1) {
            EventLoop eventLoop$kotlinx_coroutines_core = ThreadLocalEventLoop.INSTANCE.getEventLoop$kotlinx_coroutines_core();
            if (z && eventLoop$kotlinx_coroutines_core.isUnconfinedQueueEmpty()) {
                return false;
            }
            if (eventLoop$kotlinx_coroutines_core.isUnconfinedLoopActive()) {
                dispatchedContinuation._state = obj;
                dispatchedContinuation.resumeMode = i;
                eventLoop$kotlinx_coroutines_core.dispatchUnconfined(dispatchedContinuation);
                return true;
            }
            DispatchedTask dispatchedTask = dispatchedContinuation;
            eventLoop$kotlinx_coroutines_core.incrementUseCount(true);
            try {
                function0.invoke();
                do {
                } while (eventLoop$kotlinx_coroutines_core.processUnconfinedEvent());
                InlineMarker.finallyStart(1);
            } catch (Throwable th) {
                InlineMarker.finallyStart(1);
                eventLoop$kotlinx_coroutines_core.decrementUseCount(true);
                InlineMarker.finallyEnd(1);
                throw th;
            }
            eventLoop$kotlinx_coroutines_core.decrementUseCount(true);
            InlineMarker.finallyEnd(1);
            return false;
        }
        throw new AssertionError();
    }

    static /* synthetic */ boolean executeUnconfined$default(DispatchedContinuation dispatchedContinuation, Object obj, int i, boolean z, Function0 function0, int i2, Object obj2) {
        if ((i2 & 4) != 0) {
            z = false;
        }
        if (!DebugKt.getASSERTIONS_ENABLED() || i != -1) {
            EventLoop eventLoop$kotlinx_coroutines_core = ThreadLocalEventLoop.INSTANCE.getEventLoop$kotlinx_coroutines_core();
            if (z && eventLoop$kotlinx_coroutines_core.isUnconfinedQueueEmpty()) {
                return false;
            }
            if (eventLoop$kotlinx_coroutines_core.isUnconfinedLoopActive()) {
                dispatchedContinuation._state = obj;
                dispatchedContinuation.resumeMode = i;
                eventLoop$kotlinx_coroutines_core.dispatchUnconfined(dispatchedContinuation);
                return true;
            }
            DispatchedTask dispatchedTask = dispatchedContinuation;
            eventLoop$kotlinx_coroutines_core.incrementUseCount(true);
            try {
                function0.invoke();
                do {
                } while (eventLoop$kotlinx_coroutines_core.processUnconfinedEvent());
                InlineMarker.finallyStart(1);
            } catch (Throwable th) {
                InlineMarker.finallyStart(1);
                eventLoop$kotlinx_coroutines_core.decrementUseCount(true);
                InlineMarker.finallyEnd(1);
                throw th;
            }
            eventLoop$kotlinx_coroutines_core.decrementUseCount(true);
            InlineMarker.finallyEnd(1);
            return false;
        }
        throw new AssertionError();
    }
}
